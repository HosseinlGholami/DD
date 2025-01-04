import threading
from multiprocessing import Queue,Value
from app.util.util import *
from app.util.api_client import *
from app.util.image_capture import capture_image
from app.util.api_client import APIClient


def camera_maker_handler(obj,ws_queue,bg_queue,api_client):
    if obj["src"] == SRC.BGR_MAS.value and obj["data"] == BgCommands.TAKE_PICTURE_ITEM.value:
        capture_image()
        # api_client.
        pass
    else:
        print(f"camera: get wrong command obj:{obj}")

# thread for create the csv file of lidar
def camera_handler(camera_queue: Queue, ws_queue: Queue, bg_queue: Queue):
    api_client=APIClient()
    #create thread for read lidar data till end of the movment
    while True:
        obj = camera_queue.get()
        camera_maker_handler(obj,ws_queue,bg_queue,api_client)

