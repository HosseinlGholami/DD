from .serial_reader import SerialReader  # Relative import
import time

class ESP32PacketHandler:
    # Define packet types
    ESP32_COMMAND_PACKET = 0
    ESP32_HANDSHAKE_PACKET = 1
    ESP32_HEARTBEAT_PACKET = 2
    ESP32_SET_PARAM_PACKET = 3
    ESP32_GET_PARAM_PACKET = 4
    ESP32_REPORT_PACKET = 5
    ESP32_ACK_PACKET = 6

    def __init__(self, port='/dev/serial0'):
        self.serial_reader = SerialReader(port, types="", callback=self.process_message, error_callback=self.handle_error)
        self.receive_counter = 0
        # self.scan_completed = False
        # used for send data
        self.report_callback=None
        self.cmd_callback=None
        self.ack_callback=None
        self.error_callback=None

        # self.connect()

    def connect(self):
        self.serial_reader.connect()

    def handle_error(self, error_message):
        print("Error:", error_message)

    def send_packet(self, packet_type, data):
        if self.serial_reader.ser and self.serial_reader.ser.is_open:
            buffer = bytes([packet_type]) + data.encode('utf-8') + b'\r\n'
            self.serial_reader.ser.write(buffer)
            print(f"Sent: {buffer}")
        else:
            print("Serial port not open.")

    def send_command_packet(self, data):
        self.send_packet(self.ESP32_COMMAND_PACKET, data)

    def send_handshake_packet(self, data):
        self.send_packet(self.ESP32_HANDSHAKE_PACKET, data)

    def send_set_param_packet(self, address, value):
        if self.serial_reader.ser and self.serial_reader.ser.is_open:
            buffer = bytes([self.ESP32_SET_PARAM_PACKET, address]) + value.to_bytes(4, 'little') + b'\r\n'
            self.serial_reader.ser.write(buffer)
            print(f"Sent set param packet: Address={address}, Value={value}")
        else:
            print("Serial port not open.")

    def send_get_param_packet(self, address):
        if self.serial_reader.ser and self.serial_reader.ser.is_open:
            buffer = bytes([self.ESP32_GET_PARAM_PACKET, address]) + b'\r\n'
            self.serial_reader.ser.write(buffer)
            print(f"Sent get param packet: Address={address}")
        else:
            print("Serial port not open.")

    def process_message(self, message_bytes):
        if not message_bytes:
            return

        # self.receive_counter += 1
        # print(f"\n ======= NEW DATA! {self.receive_counter} ======= \n Raw data (byte by byte):")
        # for i, byte in enumerate(message_bytes):
        #     print(f"Byte {i}: 0x{byte:02X}")

        message_type = message_bytes[0]
        data = message_bytes[1:]

        if message_type == self.ESP32_ACK_PACKET:
            address = data[0]
            value = int.from_bytes(data[1:5], 'little')
            # print(f"Received ACK: Address={address}, Value={value}")
            self.ack_callback(message_bytes)

        elif message_type == self.ESP32_REPORT_PACKET:
            report_data = data.decode('utf-8').strip()
            # print(f"Received report: {report_data}")
            self.report_callback(report_data)

            # if report_data == "Scan Completed!":
            #     self.scan_completed = True
            # return report_data

        elif message_type == self.ESP32_COMMAND_PACKET:
            command_data = data.decode('utf-8').strip()
            # print(f"Received command: {command_data}")
            self.cmd_callback(command_data)

        # elif message_type == self.ESP32_HEARTBEAT_PACKET:
        #     print("Received heartbeat")

        else:
            print(f"Unknown packet type: {message_type}")
            self.error_callback(message_bytes)

    def start_reading(self,report_callback,cmd_callback,ack_callback,error_callback):
        self.report_callback=report_callback
        self.cmd_callback=cmd_callback
        self.ack_callback=ack_callback
        self.error_callback=error_callback
        self.serial_reader.read_data()  # This will block until interrupted

    def close(self):
        self.serial_reader.close()

if __name__ == '__main__':
    packet_handler = ESP32PacketHandler('/dev/tty.usbserial-14440')
    def report_callback(x):
        print(f"report_callback:{x}")
    def cmd_callback(x):
        print(f"cmd_callback:{x}")
    def ack_callback(x):
        print(f"ack_callback:{x}")
    def error_callback(x):
        print(f"error_callback:{x}")

    try:
        packet_handler.start_reading(report_callback,cmd_callback,ack_callback,error_callback) 
    except KeyboardInterrupt:
        packet_handler.close()
