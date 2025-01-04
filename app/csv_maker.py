from random import randrange
import threading

import json


from multiprocessing import Queue,Value
from app.util.util import *
from app.util.lidar_lds_02 import *


MIN_ANGLE_DEGREE = 135
MAX_ANGLE_DEGREE = 180
MIN_ACCEPTABLE_DISTANCE = 20

def fetch_lidar_data(csv_queue: Queue, last_position):
    data = dict()
    data['address'] = "LDR"
    # Initialize Lidar instance
    def data_callback(distances, angles, confidences, timestamp):
        # close the angel:
        important_angles = angles[(angles > degree_to_radians(MIN_ANGLE_DEGREE)) & (angles < degree_to_radians(MAX_ANGLE_DEGREE))]
        important_distances = distances[(angles > degree_to_radians(MIN_ANGLE_DEGREE)) & (angles < degree_to_radians(MAX_ANGLE_DEGREE))]

        # remove close point since it cannot read it and it's noise:
        important_angles = important_angles[important_distances > MIN_ACCEPTABLE_DISTANCE]
        important_distances = important_distances[important_distances > MIN_ACCEPTABLE_DISTANCE]

        if len(important_distances):
            # change polar to cartesian
            x, z = pol2cart(important_distances, important_angles)

            # send event to csv_maker_handler
            data['x']= x
            data['z'] = z
            if last_position.value >= 0:
                send_event_process(csv_queue,"DV",data)


    # Main Execution
    LIDAR_PORT = os.getenv("LIDAR_SERIAL")
    lidar = Lidar(port=LIDAR_PORT, min_confidence_level=200, callback=data_callback)
    while True:
        # it's blocking and runs callbacks
        lidar.get_lidar_packets()




def csv_maker_handler(data,ws_queue,bg_queue,point_cloud,last_position):
    address = data['address']
    if  address== ReportAddress.REPORT_FORWARD_POSITION.value:
        last_position.value = data['data']
        point_cloud[last_position.value]=[]
        # print(f"POS DATA : {last_position.value}")

    elif address == ReportAddress.REPORT_PROCESS_END.value:
        # save the csv file:
        with open("A.json", 'w') as json_file:
            json.dump(point_cloud, json_file, indent=4) 
        send_event_process(bg_queue,"CSV",data)
    elif address == "LDR":
        X = data["x"]
        y =last_position.value
        Z = data["z"]
        # print(f"LIDAR DATA: X:{X} Y:{y} Z:{Z}")
        # for i in range(len(X)):
            # send_point_cloud_to_front_app(ws_queue,X[i],y,Z[i])
        # send_point_cloud_to_front_app(ws_queue,randrange(1,100,1),randrange(1,100,1),randrange(1,100,1))
        point_cloud[last_position.value].append((X.tolist(),Z.tolist()))

        # send_event_process(bg_queue,"CSV",data)
    else:
        # point_cloud[last_position.value] = []
        pass


# thread for create the csv file of lidar
def csv_handler(csv_queue: Queue, ws_queue: Queue, bg_queue: Queue):
    point_cloud = dict()
    last_position = Value('i', -1)

    # clear the queues
    # clear_queue(csv_queue)
    last_position.value = -1
    print(f"START_THE_PROCESS XX{last_position.value}XX")

    # Start the data fetching in a separate thread
    threading.Thread(target=fetch_lidar_data, args=(csv_queue,last_position), daemon=True).start()

    #create thread for read lidar data till end of the movment
    while True:
        obj = csv_queue.get()
        csv_maker_handler(obj["data"],ws_queue,bg_queue,point_cloud,last_position)
    