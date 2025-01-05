from multiprocessing import Queue , Process ,Manager
import gc

from app.camera_maker import *
from app.csv_maker import *
from app.util.util import *



def process_msg(src , data, shared_resources):
    csv_queue = shared_resources.queues["csv_queue"]
    # camera_queue = shared_resources.queues["camera_queue"]
    esp32_queue = shared_resources.queues["esp32_queue"]
    ws_queue = shared_resources.queues["ws_queue"]
    barcode = shared_resources.working_mode.value
    
    # start command
    if src== SRC.API_MAS.value and data == BgCommands.START_PROCESS.value:
        # 1- send start command to esp32 STARTPROCESS COMMAND form api
        print("SEND START COMMAND TO ESP32 to find home")
        data_dict = create_data_dict(PacketType.DD_COMMAND_PACKET.value,CommandType.UART_START_MOTOR.value,-1)
        send_event_process(esp32_queue,src,data_dict)

        # 2- start camera process to start taking picture
        # start 
        # send_event_process(camera_queue,SRC.BGR_MAS.value,BgCommands.TAKE_PICTURE_ITEM.value)
    
    ####################################################################################################
    #############################             LIDAR FLOW          ######################################
    ####################################################################################################
    # 1-1 get acknolage of the start command form esp32
    elif data["type"] == PacketType.DD_COMMAND_PACKET.value  and src== SRC.ESP_RCV.value and data["address"] ==CommandType.UART_START_MOTOR.value:
        print("ACK OF the UART_START_SCAN_NRM command PACKET CREATE A CSV PROCESS")
        if not CSV_process_ref["process"].is_alive():
            CSV_process_ref["process"].start()
        else:
            print("the process is still alive!")
    # 1-2 motor reached home place
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  ReportAddress.REPORT_REACH_HOME.value:
        print(f"ReportAddress.REPORT_REACH_HOME.value ===>data-raw{data}")
        send_socket_to_front_app(ws_queue, cmd="start_scan")
    # 1-3 motor send fpos and we send it to csv task
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  ReportAddress.REPORT_FORWARD_POSITION.value:
        # print(f"ReportAddress.REPORT_FORWARD_POSITION.value ===>data-raw{data}")
        send_event_process(csv_queue,src,data)
    # 1-4 motor reached the end 
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  ReportAddress.REPORT_REACH_END.value:
        print(f"ReportAddress.REPORT_REACH_END.value ===>data-raw{data}")
        send_event_process(csv_queue,src,data)
        send_socket_to_front_app(ws_queue, cmd="end_scan")
    # 1-5 esp send process end and we kill the csv proess
    elif src== SRC.ESP_RCV.value and data["type"] == PacketType.DD_REPORT_PACKET.value  and  ReportAddress.REPORT_PROCESS_END.value:
        if shared_resources.processes["csv_process"].is_alive():
            shared_resources.processes["csv_process"] .terminate()
            shared_resources.processes["csv_process"] .join()  
            shared_resources.processes["csv_process"]  = None
            print("CSV process terminated.")
            #TODO: STOP LIDAR
            shared_resources.processes["csv_process"] = Process(target=csv_handler, args=(shared_resources,))
            gc.collect()  # Force garbage collection to free up memory
            # clear the working mode
            shared_resources.working_mode.value = ""
    if src== SRC.API_MAS.value and data == BgCommands.STOP_PROCESS.value:
        # 1- send stop command to from api to kill the csv process
        print("SEND STOP COMMAND TO STOP THE CSV TASK")
        data_dict = create_data_dict(PacketType.DD_COMMAND_PACKET.value,CommandType.UART_STOP_MOTOR.value,-1)
        send_event_process(esp32_queue,src,data_dict)
        #TODO: STOP LIDAR

        # 2- stop camera process to start taking picture
        # TODO
    

    else:
        print(f"unhandle command src:{get_name(SRC,src)},data:{get_name(BgCommands,data)} ")



def bg_controller(shared_resources):
    shared_resources.processes["csv_process"] = Process(target=csv_handler, args=(shared_resources,))
    shared_resources.processes["camera_process"] = Process(target=camera_handler, args=(shared_resources,))

    while True:
        obj = shared_resources.queues["bg_queue"].get()
        process_msg(obj["src"],obj["data"],shared_resources)

