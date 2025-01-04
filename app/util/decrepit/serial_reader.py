import serial
import time

class SerialReader:
    def __init__(self, port, baudrate=115200, types="utf" ,callback=None, error_callback=None):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.callback = callback
        self.error_callback = error_callback
        self.buffer_list = bytearray()  # Buffer to hold incoming bytes
        self.receive_counter = 0  # Counter for received messages
        self.types = types

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            time.sleep(2)  # Allow time for the connection to establish
            print("Serial connection established.")
        except serial.SerialException as e:
            if self.error_callback:
                self.error_callback(f"Connection error: {e}")
            print(f"Failed to connect to {self.port}. Retrying in 5 seconds...")
            time.sleep(5)  # Delay before retrying
            self.connect()  # Retry connection

    def read_data(self):
        if self.ser is not None and self.ser.is_open:
            while True:  # This loop will block until new data is received
                try:
                    raw_data = self.ser.read(1024)  # Read a chunk of data
                    self.buffer_list.extend(raw_data)  # Add to the buffer

                    while True:  # Process messages in the buffer
                        try:
                            newline_index = self.buffer_list.index(13)  # ASCII code for \r
                            if newline_index + 1 < len(self.buffer_list) and self.buffer_list[newline_index + 1] == 10:  # Check for \n
                                message = self.buffer_list[:newline_index]  # Extract the complete message
                                del self.buffer_list[:newline_index + 2]  # Remove processed bytes
                                self.receive_counter += 1
                                message_bytes = bytes(message)
                                # print(f"\n ======= NEW DATA! {self.receive_counter} ======= \n Raw data (byte by byte):")
                                # for i, byte in enumerate(message_bytes):
                                #     print(f"Byte {i}: 0x{byte:02X}")
                                if self.callback:
                                    if self.types == "utf":
                                        self.callback(message_bytes.decode('utf-8'))
                                    else:
                                        self.callback(message_bytes)
                            else:
                                break  # Exit if no complete message is found
                        except ValueError:
                            break  # No complete message found in buffer

                except serial.SerialException as e:
                    if self.error_callback:
                        self.error_callback(f"Read error: {e}")
                    break  # Exit the loop if an error occurs
                except UnicodeDecodeError as e:
                    if self.error_callback:
                        self.error_callback(f"Decode error: {e}")

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
            print("Serial connection closed.")

if __name__ == '__main__':
    def process_data(data):
        # Custom logic to process the raw data
        print("Received Data:", data)

    def handle_error(error_message):
        # Custom logic to handle errors
        print("Error:", error_message)

    # reader = SerialReader('/dev/tty.usbserial-14440', callback=process_data, error_callback=handle_error)  # Replace with your serial port
    reader = SerialReader('/dev/tty.cu.usbserial-0001', callback=process_data, error_callback=handle_error)  # Replace with your serial port
    try:
        reader.connect()
        reader.read_data()  # This will block until interrupted
    except KeyboardInterrupt:
        reader.close()
