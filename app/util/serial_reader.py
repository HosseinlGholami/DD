# serial_reader.py
import serial
import time

class SerialReader:
    def __init__(self, port, baudrate=115200, callback=None, error_callback=None):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.callback = callback
        if error_callback == None:
            self.error_callback = self.error_handler
        else:
            self.error_callback = error_callback

        self.buffer = bytearray()  # Buffer to hold incoming bytes

    def connect(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            time.sleep(0.1)  # Allow time for the connection to establish
            print("Serial connection established.")
        except serial.SerialException as e:
            self.handle_error(f"Connection error: {e}")
            print("Retrying connection in 5 seconds...")
            time.sleep(5)
            self.connect()  # Retry connection

    def retry_connection(self):
        while True:
            try:
                self.connect()  # Attempt to reconnect
                break  # Exit the loop if successful
            except Exception as e:
                self.handle_error(f"Retry connection error: {e}")
                time.sleep(5)  # Wait before retrying
                
    def read_data(self):
        if self.ser is not None and self.ser.is_open:
            try:
                raw_data = self.ser.read()  # Read a chunk of data
                self.buffer.extend(raw_data)  # Add to the buffer

                if b'\r\n' in self.buffer:
                    messages = self.buffer.split(b'\r\n')  # Split the buffer by message terminators
                    self.buffer = messages.pop()  # Keep any incomplete message in the buffer

                    for message in messages:
                        self.process_message(message)

            except serial.SerialException as e:
                self.handle_error(f"Read error: {e}")
                self.close()  # Close the serial connection on error
                self.retry_connection()  # Attempt to reconnect
        else:
            print("Serial port is not open. Retrying connection...")
            self.retry_connection()

    def process_message(self, message):
        if self.callback:
            self.callback(message)  # No decoding, raw message is passed

    def send_data(self, data):
        """Send raw data over the serial port."""
        if self.ser is not None and self.ser.is_open:
            try:
                self.ser.write(data)
                # print(f"uart_sent_packet: {data.hex()}")
            except serial.SerialException as e:
                self.handle_error(f"Send error: {e}")

    def handle_error(self, error_message):
        if self.error_callback:
            self.error_callback(error_message)

    def close(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
            print("Serial connection closed.")
    
    def error_handler(self,error_message):
        # Handle any errors here
        print(f"Error: {error_message}")
        

    def run(self):
        """Main loop to send and receive data."""
        self.connect()
        try:
            while True:
                self.read_data()  # Continuously read data
        except KeyboardInterrupt:
            print("Stopping the reader.")
        finally:
            self.close()
            
if __name__ == "__main__":
    import threading
    def message_handler(message):
        # Process the received message here
        print(f"Received message: {message}")

    SERIAL_PORT = '/dev/tty.usbserial-14120'
    myserial = SerialReader(port=SERIAL_PORT, callback=message_handler)
    def send_command(serial_reader, command):
        """Function to send a command via the serial reader."""
        time.sleep(5)  # Optional: Wait before sending the command

        while True:
            time.sleep(3)  # Optional: Wait before sending the command
            serial_reader.send_data(command)


    # Start a thread to send a command
    command_to_send = b'112341000000'  # Replace with your actual command
    send_thread = threading.Thread(target=send_command, args=(myserial, command_to_send))
    send_thread.start()

    myserial.run()

