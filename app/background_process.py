from multiprocessing import Queue , Process ,Manager
import time , random

from app.camera_maker import *
from app.csv_maker import *
from app.util.util import *

from app.util.strip_controler import *
from app.util.gpio_conteoller import *


def process_msg(src , data, shared_resources,api_clinet):
    bg_queue = shared_resources.queues["bg_queue"]
    csv_queue = shared_resources.queues["csv_queue"]
    camera_queue = shared_resources.queues["camera_queue"]
    esp32_queue = shared_resources.queues["esp32_queue"]
    ws_queue = shared_resources.queues["ws_queue"]
    barcode = shared_resources.working_mode.value
    
    ####################################################################################################
    #############################             START FLOW          ######################################
    ####################################################################################################
    if src== SRC.API_MAS.value and data == BgCommands.START_PROCESS.value:
        print("SEND BgCommands.START_PROCESS.value")
        # 0- send start scan
        send_socket_to_front_app(ws_queue, cmd="start_scan")
        
        # 1- send event to camera task to takign the picture
        send_event_process(camera_queue,SRC.BGR_MAS.value,BgCommands.TAKE_PICTURE_ITEM.value)
        # 1-1 do flush
        fill_color((255,255,255))
        #2-0: start the lidar
        lidar_controll(True)
        
        # add a dummy time for take picture first then goes for lidar flow
        time.sleep(1)

        # TODO START LIDAR
        # 2- send start command to esp32 STARTPROCESS COMMAND form api
        data_dict = create_data_dict(PacketType.DD_COMMAND_PACKET.value,CommandType.UART_START_SCAN_NRM.value,-1)
        send_event_process(esp32_queue,src,data_dict)


    ####################################################################################################
    #############################             CAMERA FLOW          ######################################
    ####################################################################################################
    elif src == SRC.CAM_MAS.value and data =="ITEM_RDY": 
        # pictue is taken we have to call api and inform the front application
        # 1- send img_ready to fetch the image url form /img-get api
        send_socket_to_front_app(ws_queue, cmd="img_ready")
        # 2- call the api async
        async_api_call(api_clinet, "send_image", bg_queue, barcode)


    elif src == SRC.CAM_MAS.value and data =="CALIB_RDY": 
        # pictue is taken we have to call api
        # 1- api call async
        async_api_call(api_clinet, "camera_calibration", bg_queue, barcode)


    ####################################################################################################
    #############################             LIDAR FLOW          ######################################
    ####################################################################################################
    # 1-1 get acknolage of the start command form esp32
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_COMMAND_PACKET.value  and data["address"] == CommandType.UART_START_SCAN_NRM.value:
        print("ACK OF the UART_START_SCAN_NRM command PACKET CREATE A CSV PROCESS")
        start_the_process(shared_resources,"csv_process")
    # 1-2 motor reached home place
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  data["address"] == ReportAddress.REPORT_REACH_HOME.value:
        print(f"ReportAddress.REPORT_REACH_HOME.value ===>data-raw{data}")
    # 1-3 motor send fpos and we send it to csv task
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  data["address"] == ReportAddress.REPORT_FORWARD_POSITION.value:
        # print(f"ReportAddress.REPORT_FORWARD_POSITION.value ===>data-raw{data}")
        send_event_process(csv_queue,src,data)
    # 1-4 motor reached the end 
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  data["address"] == ReportAddress.REPORT_REACH_END.value:
        print(f"ReportAddress.REPORT_REACH_END.value ===>data-raw{data}")
        send_event_process(csv_queue,src,data)
    # 1-5 
    elif src== SRC.CSV_MAS.value:
        kill_the_process(shared_resources, "csv_process",csv_handler)   
        
        # STOP LIDAR
        lidar_controll(False)
        print("SOOOOSK -1")
        # call the api async
        async_api_call(api_clinet, "send_point_cloud", bg_queue, barcode)
        print("SOOOOSK -2")

    ####################################################################################################
    ##########################             END THE PROCESS            ##################################
    ####################################################################################################

    # esp send process end and we kill the csv proess
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  data["address"] == ReportAddress.REPORT_PROCESS_END.value:
        print(f"ReportAddress.REPORT_PROCESS_END.value ===>data-raw{data}")
        # send_event_process(csv_queue,src,data)
        # send_socket_to_front_app(ws_queue, cmd="process_end")
        # clear the working mode

    # got result from api
    elif src == SRC.API_CL_MAS.value:
        if data["method_name"] == "send_point_cloud":
            print(f"point clousd: API RES: {data}")
            # it means it has correct response from the point cloud
            # so we ignore the camera data 
            # and send this response to front application
            if data["pc_length"] > 0: 
                print("6894286SAAAAAAAAAAAAAAAKKKKKKKKKKKKKKKKKKKKKIIIIIIIIIIIINEEEEEEEEEEEEEE")
                report_data = {
                    "w": round(data["pc_width"]   ,2),
                    "h": round(data["pc_height"]  ,2),
                    "l": round(data["pc_length"]  ,2),
                    "weight": round(data["weight"],2),
                }
                # DO GREEN 
                fill_color((255,0,0))
                send_socket_to_front_app(ws_queue, cmd="end_scan",data=[report_data])
            else:
                print("lidar cannot get data ---->>> WE HAVE TO WAIE TILL THE IMAGE API GET RESPONSE")
        elif data["method_name"] == "send_image":
            print(f"SAAAAAAAAAAAAAAAKKKKKKKKKKKKKKKKKKKKKIIIIIIIIIIIINEEEEEEEEEEEEEE{data}")
            if "pc_length" not in data:
                print(f"image API RES: {data}")
                report_data = {
                    "w": round(data["image_width"] ,2),
                    "h": round(data["image_height"],2),
                    "l": round(data["image_length"],2),
                    "weight": round(data["weight"] ,2),
                }
                # DO GREEN 
                fill_color((255,0,0))
                send_socket_to_front_app(ws_queue, cmd="end_scan",data=[report_data])
            else:
                print(f"we ignore the image API but: {data}")

        elif data["method_name"] == "camera_calibration":
            print("callibration done ")
        else:
            print("GOT INVALID METHOD NAME")


    ####################################################################################################
    #############################             STOP FLOW           ######################################
    ####################################################################################################
    elif src== SRC.API_MAS.value and data == BgCommands.STOP_PROCESS.value:
        print("SEND STOP COMMAND TO STOP THE CSV TASK")
        # 1- send stop command to from api to kill the csv process
        kill_the_process(shared_resources, "csv_process",csv_handler)   
        
        shared_resources.working_mode.value = ""

        # 2- send event to esp32 to restart task
        # data_dict = create_data_dict(PacketType.DD_COMMAND_PACKET.value,CommandType.UART_STOP_MOTOR.value,-1)
        # send_event_process(esp32_queue,src,data_dict)
        
        #3- STOP LIDAR
        lidar_controll(False)
        fill_color((0,0,0))

        # add a dummy time for take picture first then goes for lidar flow
        
        

    elif src== SRC.API_MAS.value and data == BgCommands.END_PROCESS.value:
        print("STTTTTTTTTTTTTTTTOOOOOOOOOOOOPPPPPPPPPPPPPPPPP")
        shared_resources.working_mode.value = ""
        fill_color((0,0,0))
        # TODO: run api call to send supernova



    else:
        print(f"unhandle command src:{get_name(SRC,src)},data:{data} ")



def bg_controller(shared_resources):
    shared_resources.processes["csv_process"] = Process(target=csv_handler, args=(shared_resources,))
    shared_resources.processes["camera_process"] = Process(target=camera_handler, args=(shared_resources,))
    start_the_process(shared_resources,"camera_process")
    api_clinet = APIClient()
    while True:
        obj = shared_resources.queues["bg_queue"].get()
        process_msg(obj["src"],obj["data"],shared_resources,api_clinet)

