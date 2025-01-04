
if __name__ == "__main__":
    from util.util import *
    from util.protocol_handler import UARTProtocolHandler
elif __name__ == "app.esp32_process":
    from app.util.util import *
    from app.util.protocol_handler import UARTProtocolHandler
else:
    print("__name__")
    print(__name__)
    print("__name__")

import time, os
from multiprocessing import Process,Queue

def esp32_connection_reciver(esp32_queue:Queue,myserial:UARTProtocolHandler):

    def handle_received_packet(raw_data):
        # if b'[0m' in raw_data:
        #     # print(f"ESP SAYS: {raw_data}")
        #     return
        if raw_data and len(raw_data) == myserial.PACKET_SIZE:
            packet = myserial.pars_packet(raw_data)
            send_event_process(esp32_queue,SRC.ESP_RCV.value,packet)
    
    myserial.run(handle_received_packet)



def process_msg(obj,serial_client,shared_resources):
    try:
        cmd_type = obj["data"]["type"]
    except:
        cmd_type = None
    server_cmd_condition = cmd_type == PacketType.DD_HEARTBEAT_PACKET.value
    server_cmd_condition = server_cmd_condition or cmd_type == PacketType.DD_GET_PARAM_PACKET.value
    server_cmd_condition = server_cmd_condition or cmd_type == PacketType.DD_SET_PARAM_PACKET.value
    
    # get queue form shared resources    
    bg_queue = shared_resources.queues["bg_queue"]
    server_queue = shared_resources.queues["server_queue"]

    # ==============    RELATED TO SERVER    ==============
    # if it's commands from server and it's GET SET HBT
    if obj["src"] == SRC.SRV_RCV.value and server_cmd_condition:    
        # print(f"WE SEND FOR ESP32 {data}")
        serial_client.send_packet_raw(obj["data"])
    # if it's command is from esp32 and commands are  GET,SET,HBT we have to send it to server process
    elif obj["src"] == SRC.ESP_RCV.value and server_cmd_condition:
        send_event_process(server_queue,obj["src"],obj["data"])
    
    # ==============    RELATED TO PROCESS    ==============
    #  1 : from command form api task to send uart start motor
    elif obj["src"] == SRC.API_MAS.value and cmd_type == PacketType.DD_COMMAND_PACKET.value  and obj["data"]["address"] ==CommandType.UART_START_MOTOR.value:
        serial_client.send_packet(obj["data"]["type"], obj["data"]["address"], obj["data"]["data"])
    # 2 :related to ack of command packet for starting
    elif obj["src"] == SRC.ESP_RCV.value and cmd_type == PacketType.DD_COMMAND_PACKET.value and obj["data"]["address"] ==CommandType.UART_START_MOTOR.value:
        send_event_process(bg_queue,obj["src"],obj["data"])
    #  3 : get data from esp32 
    elif obj["src"]== SRC.ESP_RCV.value and cmd_type == PacketType.DD_REPORT_PACKET.value:
        send_event_process(bg_queue,obj["src"],obj["data"])


    else:
        print(f"wrong condition: src: {obj["src"]} data: {obj["data"]}")
            



def esp32_process(shared_resources):
    # prepare serial class
    SERIAL_PORT = os.getenv("ESP32_SERIAL")
    print(f"===>>>   SERIAL_PORT --> {SERIAL_PORT} ")
    
    esp32_queue = shared_resources.queues["esp32_queue"]
    serial_client = UARTProtocolHandler(serial_port=SERIAL_PORT)

    # start reciver process
    process = Process(target=esp32_connection_reciver, args=(esp32_queue,serial_client))
    process.start()

    # connect to serial
    serial_client.connect()
    
    while True:
        obj =esp32_queue.get()
        process_msg(obj,
                    serial_client,
                    shared_resources)



if __name__ == "__main__":
    esp32_queue = Queue()
    server_queue = Queue()
    process = Process(target=esp32_process, args=(esp32_queue,server_queue))
    process.start()

