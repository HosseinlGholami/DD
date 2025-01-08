import threading
from multiprocessing import Queue,Value
from app.util.util import *
from app.util.api_client import *
from app.util.image_capture import capture_image


def camera_maker_handler(obj,bg_queue):
    if obj["src"] == SRC.BGR_MAS.value and obj["data"] == BgCommands.TAKE_PICTURE_ITEM.value:
        capture_image()
        send_event_process(bg_queue,SRC.CAM_MAS.value,"ITEM_RDY")
    elif obj["src"] == SRC.API_MAS.value and obj["data"] == BgCommands.TAKE_PICTURE_CALIB.value:
        capture_image()
        send_event_process(bg_queue,SRC.CAM_MAS.value,"CALIB_RDY")
    else:
        print(f"camera: get wrong command obj:{obj}")

# thread for create the csv file of lidar
def camera_handler(shared_resources):
    camera_queue = shared_resources.queues["camera_queue"]
    bg_queue = shared_resources.queues["bg_queue"]

    # clear the queues
    shared_resources.clear_queue("camera_queue")

    #create thread for read lidar data till end of the movment
    while True:
        obj = camera_queue.get()
        camera_maker_handler(obj,bg_queue)

