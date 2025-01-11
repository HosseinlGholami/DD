from enum import Enum
import gc
from multiprocessing import Process
import threading

def send_socket_to_front_app(queue,cmd,data={}):
    meta = {'cmd':cmd,'data':data}  
    queue.put(meta)  


class BgCommands(Enum):
    START_PROCESS =0
    STOP_PROCESS =1
    TAKE_PICTURE_ITEM=2
    TAKE_PICTURE_CALIB=3    


class PacketType(Enum):
    DD_HEARTBEAT_PACKET=0 # DONE
    DD_PING_PONG_PACKET=1
    DD_REPORT_PACKET=2  #DONE
    DD_COMMAND_PACKET=3    
    DD_GET_PARAM_PACKET=4 #DONE 
    DD_SET_PARAM_PACKET=5 #DONE



class CommandType(Enum):
    UART_START_SCAN_NRM = 0 
    UART_START_SCAN_DWAY = 1 
    UART_GO_HOME = 2
    UART_GO_END =3

class SRC(Enum):
    SRV_RCV=0
    SRV_MAS=1
    ESP_RCV=2
    SER_MAS=3
    BGR_MAS=4
    API_MAS=5
    CSV_MAS=6
    LDR_MAS=7
    CAM_MAS=8
    API_CL_MAS=9


class ReportAddress(Enum):
    REPORT_FORWARD_POSITION =0
    REPORT_BACKWARD_POSITION =1
    REPORT_REACH_END =2
    REPORT_REACH_HOME =3
    REPORT_PROCESS_END =4
    


def get_name(enum_class, value):
    for member in enum_class:
        if member.value == value:
            return member.name
    return None

def create_data_dict(types,address,data):
    data_dict = {
        "type": types,
        "address": address,
        "data": data, 
    }
    return data_dict

def send_event_process(queue,src,data_dict):
    data = {"src":src,"data":data_dict}
    queue.put(data)



def start_the_process(shared_resources, process_name):
    if not shared_resources.processes[process_name].is_alive():
        shared_resources.processes[process_name].start()
    else:
        print("the process is still alive!")


def kill_the_process(shared_resources, process_name,task_handler):
    # kill the process
    if shared_resources.processes[process_name].is_alive():
        shared_resources.processes[process_name] .terminate()
        shared_resources.processes[process_name] .join()  
        shared_resources.processes[process_name]  = None
        print(f"{process_name} terminated.")
        shared_resources.processes[process_name] = Process(target=task_handler, args=(shared_resources,))
        gc.collect()

    
def run_api_call(api_client, method, queue, *args, **kwargs):
    try:
        response = method(*args, **kwargs)
        data = {"src":SRC.API_CL_MAS.value,"data":response}
        queue.put(data)
    except Exception as e:
        queue.put((False, str(e)))


def async_api_call(api_client, method_name, queue, *args, **kwargs):
    method = getattr(api_client, method_name, None)
    if method is None:
        raise ValueError(f"Method {method_name} does not exist on APIClient.")

    thread = threading.Thread(target=run_api_call, args=(api_client, method, queue, *args), kwargs=kwargs)
    thread.start()