from random import randrange
import threading

import json, os , csv


from multiprocessing import Queue,Value
from app.util.util import *
from app.util.lidar_lds_02 import *
import numpy as np

MIN_ANGLE_DEGREE = 100
MAX_ANGLE_DEGREE = 260
MIN_ACCEPTABLE_DISTANCE = 20

def fetch_lidar_data(csv_queue: Queue):
    # Initialize Lidar instance
    def data_callback(distances, angles, confidences, timestamp):
        # close the angel:
        mask = (angles > degree_to_radians(MIN_ANGLE_DEGREE)) & (angles < degree_to_radians(MAX_ANGLE_DEGREE))
        important_angles = angles[mask]
        important_distances = distances[mask]
        important_confidences = confidences[mask]

        # remove close point since it cannot read it and it's noise:
        mask = important_distances > MIN_ACCEPTABLE_DISTANCE
        important_angles = important_angles[mask]
        important_distances = important_distances[mask]
        important_confidences = important_confidences[mask]
        
        if len(important_distances):
            # change polar to cartesian
            z, x = pol2cart(important_distances, important_angles)
            nx = []
            nz = []
            for index in range(len(x)):
                if 500>x[index]>-500 and 0>z[index]>-650:
                    nx.append(round(x[index], 3))
                    nz.append(round(z[index], 3))
            
            if len(nx)>0:
                data = dict()
                data['address'] = "LDR"

                # send event to csv_maker_handler
                data['x']= nx
                data['z'] = nz
                data['conf'] = important_confidences

                send_event_process(csv_queue,"DV",data)


    # Main Execution
    LIDAR_PORT = os.getenv("LIDAR_SERIAL")
    print(f"===>>>  LIDAR_SERIAL:  LIDAR_PORT --> {LIDAR_PORT} ")

    lidar = Lidar(port=LIDAR_PORT, min_confidence_level=200, callback=data_callback)
    while True:
        # it's blocking and runs callbacks
        lidar.get_lidar_packets()


def csv_maker_handler(data,ws_queue,bg_queue,point_cloud,last_position,sample_index):
    if  data['address'] == ReportAddress.REPORT_FORWARD_POSITION.value:
        last_position.value = data['data']
        # print(f" {last_position.value} ===")
        
    elif data['address'] == "LDR":
        # print(f" {last_position.value} ==>  {len(data['x'])} - {len(data['z'])} - {len(data['conf'])} ")        
        if last_position.value>0:
            new_point = []
            for index in range(len(data['x'])):
                value = {
                    "id" : sample_index.value,
                    "x": data['x'][index],
                    "y": last_position.value,
                    "z": data['z'][index],
                    "conf": data['conf'][index]
                }
                # save to list for file saveing 
                new_point.append(value)
                sample_index.value+=1

            point_cloud+=new_point            
            # send to front application
            send_socket_to_front_app(ws_queue, cmd="plot",data=new_point)

        # elif last_position.value in [100,200,300,400,500,600,700]:
        #     batch = last_position.value
        #     print(f"bbbbbbbbbbbbb--->{batch}")
        #     # send to front application
        #     send_socket_to_front_app(ws_queue, cmd="plot",data=point_cloud[batch:batch+1])

    #     # send_event_process(bg_queue,"CSV",data)
    elif data['address'] == ReportAddress.REPORT_REACH_END.value:
        # save the csv file:        
        with open('temp.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header
            writer.writerow(['','x', 'y', 'z','conf'])
            # Write the data
            for item in point_cloud:
                writer.writerow([item['id'],item['x'], item['y'], item['z'],item['conf']])

        # send event to kill the process since the csv file is created
        send_event_process(bg_queue,SRC.CSV_MAS.value,data)

    # elif data['address'] == ReportAddress.REPORT_PROCESS_END.value:
        # send event to bg to kill the process
        # send_event_process(bg_queue,SRC.CSV_MAS.value,data)

    else:
        print(f"unhandle command on csv maker {data} , last_position {last_position.value} ")
        pass


# thread for create the csv file of lidar
def csv_handler(shared_resources):
    csv_queue = shared_resources.queues["csv_queue"]
    ws_queue = shared_resources.queues["ws_queue"]
    bg_queue = shared_resources.queues["bg_queue"]

    point_cloud = list()
    last_position = Value('i', -1)
    sample_index = Value('i', -1)

    # clear the queues
    shared_resources.clear_queue("csv_queue")
    last_position.value = -1
    sample_index.value =0
    # Start the data fetching in a separate thread
    threading.Thread(target=fetch_lidar_data, args=(csv_queue,), daemon=True).start()

    #create thread for read lidar data till end of the movment
    while True:
        obj = csv_queue.get()
        csv_maker_handler(obj["data"],ws_queue,bg_queue,point_cloud,last_position,sample_index)
    