# protocol_handler.py
if __name__ == "__main__":
    from serial_reader import SerialReader
elif __name__ =="util.esp32_process":
    from util.util import *
    from util.serial_reader import SerialReader
elif __name__ == "app.util.protocol_handler":
    from app.util.util import *
    from app.util.serial_reader import SerialReader


import struct
import time

class UARTProtocolHandler:
    PACKET_FORMAT = '>BIBBi'  # Corresponding to the packet structure (Byte, Int, Byte, Byte, Int, Int)
    PACKET_SIZE = 11  # 11 bytes total size of the packet

    # Packet command types
    UART_HEARTBEAT_PACKET = 0
    UART_PING_PONG_PACKET = 1
    UART_REPORT_PACKET = 2
    UART_COMMAND_PACKET = 3    
    UART_GET_PARAM_PACKET = 4
    UART_SET_PARAM_PACKET = 5

    def __init__(self, serial_port):
        """Initialize and connect the serial reader."""
        self.serial_reader = SerialReader(port=serial_port, callback=self.handle_received_packet)
        self.callback = None
        
    def run(self,callback):
        self.callback = callback
        self.serial_reader.run()

    def connect(self):
        self.serial_reader.connect()

    def local_run(self):
        self.serial_reader.run()

    def handle_received_packet(self,raw_data):
        """Handle the received packet and take actions based on packet type."""
        if self.callback:
            self.callback(raw_data)
            return
        if b'[0m' in raw_data:
            print(f"ESP SAYS: {raw_data}")
            return
        
        print(f"REAL DATA: {raw_data}")
        if raw_data and len(raw_data) >= self.PACKET_SIZE:
            version, timestamp, packet_type, address, data = struct.unpack(self.PACKET_FORMAT, raw_data)
            print(f'Received packet - Version: {version}, Timestamp: {timestamp}, Type: {packet_type}, Address: {address}, Data: {data}')

            # Handle each packet type accordingly
            if packet_type == self.UART_HEARTBEAT_PACKET:
                print("Heartbeat Packet received")

            elif packet_type == self.UART_PING_PONG_PACKET:
                print("Ping-Pong Packet received")

            elif packet_type == self.UART_REPORT_PACKET:
                print("Report Packet received")
                # Process report packet (custom logic here)

            elif packet_type == self.UART_COMMAND_PACKET:
                print("Command Packet received")
                # Process command packet (custom logic here)

            elif packet_type == self.UART_GET_PARAM_PACKET:
                print("Get Param Packet received")

            elif packet_type == self.UART_SET_PARAM_PACKET:
                print("Set Param Packet received")

            else:
                print("Unknown Packet Type")

    def pars_packet (self,msg):
        packed_struct = '<BIBBi'
        data = struct.unpack(packed_struct, msg)
        return {
            "version": data[0], "timestamp": data[1], "type": data[2],
            "address": data[3], "data": data[4] , 
        }

    def create_packet(self, packet_type, address, data):
        """Create a packet based on the protocol."""
        version = 1
        timestamp = int(time.time())  # Use current time as timestamp

        return struct.pack(
            self.PACKET_FORMAT,
            version,  # 1 byte version
            timestamp,  # 4 byte timestamp
            packet_type,  # 1 byte type
            address,  # 1 byte address
            data      # 4 byte sign data Data
        )
    
    def create_packet_from_data_dict(self,data_dict):
        return struct.pack(
            self.PACKET_FORMAT,
            data_dict["version"],    # 1 byte version
            data_dict["timestamp"],  # 4 byte timestamp
            data_dict["type"],       # 1 byte type
            data_dict["address"],    # 1 byte address
            data_dict["data"]        # 4 byte sign data Data
        )

    def send_packet(self, packet_type, address, data):
        """Send a response packet over the serial port."""
        packet = self.create_packet(packet_type, address, data)
        self.serial_reader.send_data(packet)


    def send_packet_raw(self,data_dict):
        """Send a response packet over the serial port."""
        data= self.create_packet_from_data_dict(data_dict)
        res=self.serial_reader.send_data(data)
    def close(self):
        """Close the serial connection."""
        self.serial_reader.close()



if __name__ == "__main__":
    import threading
    import time


    SERIAL_PORT = '/dev/tty.usbserial-14120'
    myserial = UARTProtocolHandler(serial_port=SERIAL_PORT)

    def send_command(serial_reader,):
        """Function to send a command via the serial reader."""
        time.sleep(5)  # Optional: Wait before sending the command
        index =0
        while True:
            time.sleep(5)  # Optional: Wait before sending the command

            # sample get hbt
            serial_reader.send_packet(serial_reader.UART_HEARTBEAT_PACKET,85,-1)


            # sample get data
            # print(f"get address {index}--->>>")
            # serial_reader.send_packet(serial_reader.UART_GET_PARAM_PACKET,index,-1)
            # index+=1


            # sample set data
            # for send command after each other we need 10ms second delay unless the esp32 uart will get all data togheter.
            # print(f"get address {index}--->>>")
            # serial_reader.send_packet(serial_reader.UART_GET_PARAM_PACKET,0,-1)
            # time.sleep(0.01)
            # serial_reader.send_packet(serial_reader.UART_SET_PARAM_PACKET,0,2)
            # time.sleep(0.01)
            # serial_reader.send_packet(serial_reader.UART_GET_PARAM_PACKET,0,-1)
            # time.sleep(0.01)


    # Start a thread to send a command
    send_thread = threading.Thread(target=send_command, args=(myserial,))
    send_thread.start()

    # myserial.local_run()



    def handle_received_packet(raw_data):
        if b'[0m' in raw_data:
            print(f"ESP SAYS: {raw_data}")
            return
        
        print(f"REAL DATA: {raw_data}")
        if raw_data and len(raw_data) >= myserial.PACKET_SIZE:
            version, timestamp, packet_type, address, data = struct.unpack(myserial.PACKET_FORMAT, raw_data)
            print(f'Received packet - Version: {version}, Timestamp: {timestamp}, Type: {packet_type}, Address: {address}, Data: {data}')

            # Handle each packet type accordingly
            if packet_type == myserial.UART_HEARTBEAT_PACKET:
                print("Heartbeat Packet received")

            elif packet_type == myserial.UART_PING_PONG_PACKET:
                print("Ping-Pong Packet received")

            elif packet_type == myserial.UART_REPORT_PACKET:
                print("Report Packet received")
                # Process report packet (custom logic here)

            elif packet_type == myserial.UART_COMMAND_PACKET:
                print("Command Packet received")
                # Process command packet (custom logic here)

            elif packet_type == myserial.UART_GET_PARAM_PACKET:
                print("Get Param Packet received")

            elif packet_type == myserial.UART_SET_PARAM_PACKET:
                print("Set Param Packet received")
            else:
                print("Unknown Packet Type")

    myserial.run(handle_received_packet)

