from multiprocessing import Process , Queue
import time,os

if __name__ == "__main__":
    from util.rabbit_client import RabbitMQClient
    from util.util import *
elif __name__ == "app.server_process":
    from app.util.rabbit_client import RabbitMQClient
    from app.util.util import *


def process_msg(obj, rabbitmq_client,shared_resources,DEVICE_ID):
    
    # handle command get from server :
    if obj["src"] == SRC.SRV_RCV.value :
        # check the command type form server 
        # and if this condition are provieded send them directly to esp32
        try:
            cmd_type = obj["data"]["type"]
        except:
            cmd_type = None
        server_cmd_condition = cmd_type == PacketType.DD_HEARTBEAT_PACKET.value
        server_cmd_condition = server_cmd_condition or cmd_type == PacketType.DD_GET_PARAM_PACKET.value
        server_cmd_condition = server_cmd_condition or cmd_type == PacketType.DD_SET_PARAM_PACKET.value
        print(f"GOT : {get_name(PacketType,cmd_type)}")

        if server_cmd_condition:
            # get the esp32 queue to send commands 
            esp32_queue = shared_resources.queues["esp32_queue"]
            send_event_process(esp32_queue,obj["src"],obj["data"])
        else:
            print(f"wrong condition:  obj: {obj}")
            
    # handle command reviced from esp32 send what you get from esp32
    elif obj["src"] == SRC.ESP_RCV.value:
        TOPIC = f".DD.hub.{DEVICE_ID}"
        rabbitmq_client.send_message(TOPIC,obj["data"])
    else:
        print(f"wrong condition:  obj: {obj}")


# the process
def server_connection_reciver(server_queue:Queue, DD_BROKER_URL:str, DEVICE_ID:str):

    rabbitmq_client = RabbitMQClient(DD_BROKER_URL)
    rabbitmq_client.connect()
    
    QUEUE_NAME = f"DD-{DEVICE_ID}"
    TOPIC = f".DD.hub.{DEVICE_ID}"

    print("CONNECT TO BROKER")
    # connect with pika to broker and wait for get/set packet
    def callback(ch, method, properties, body):
        msg = rabbitmq_client.parse_message(body)
        # print(f"server recived : {msg}")
        # send to event to esp32 sender queue
        # send_event_process(TOPIC,server_queue,SRC.SRV_RCV.value,msg)
        # ch.basic_publish(exchange='amq.topic',
        #              routing_key=".DD.server.{DEVICE_ID}",
        #              body=body)
    rabbitmq_client.listen_for_messages(queue_name=QUEUE_NAME,routing_key=TOPIC,callback=callback)



def server_connection(shared_resources):
    """
    Main entry point for the server connection process.
    """

    DD_BROKER_URL = os.getenv("DD_BROKER_URL")
    DEVICE_ID = os.getenv("DEVICE_ID")

    # Start the server receiver process
    process = Process(target=server_connection_reciver, args=(shared_resources.queues["server_queue"],DD_BROKER_URL,DEVICE_ID,))
    process.start()

    # Initialize RabbitMQ client

    print(f"=====>> DD_BROKER_URL: {DD_BROKER_URL}")
    rabbitmq_client = RabbitMQClient(DD_BROKER_URL)
    rabbitmq_client.connect()

    # get from server queue to handle events
    server_queue = shared_resources.queues["server_queue"]
    while True:
        obj = server_queue.get()
        process_msg(
            obj,
            rabbitmq_client,
            shared_resources,
            DEVICE_ID
        )


    handle_server_messages(rabbitmq_client, shared_resources, )

if __name__ == "__main__":
    esp32_queue = Queue()
    server_queue = Queue()
    process = Process(target=server_connection, args=(esp32_queue,server_queue))
    process.start()
