
def send_socket_to_front_app(queue,cmd,data={}):
    meta = {'cmd':cmd,'data':data}  
    queue.put(meta)  

from enum import Enum



class BgCommands(Enum):
    START_PROCESS =0
    STOP_PROCESS =1


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
