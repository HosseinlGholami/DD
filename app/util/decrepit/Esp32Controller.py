from multiprocessing import Process, Queue
import time
from Util.esp32_handler import ESP32PacketHandler  


class ESP32Reciver:
    def __init__(self, report_queue,cmd_queue, esp_connection):
        self.esp_connection = esp_connection
        self.report_queue = report_queue
        self.cmd_queue = cmd_queue

    def report_callback(self,data):
        # put to report queue
        pass

    def cmd_callback(self,data):
        # put to cmd queue
        pass

    def ack_callback(self,x):
        print(f"ack_callback:{x}")

    def error_callback(self,x):
        print(f"error_callback:{x}")

    def generate_data(self):
        try:
            print(f"LidarProducer started ...")
            self.esp_connection.connect()
            self.esp_connection.start_reading(self.report_callback,self.cmd_callback,self.error_callback,self.error_callback)
        except Exception as err:
            print(f"LidarProducer stopped ...")
            print(err)

class ESP32Commander:
    CMD=1
    GET=2
    SET=3
    
    def __init__(self, cmd_queue, esp_connection):
        self.cmd_queue = cmd_queue
        self.esp_connection = esp_connection

    def ControllQueue(self):
        while True:
            try:
                message = self.cmd_queue.get(timeout=0.001)  # 1 milliseconds timeout
                if message[0] == self.CMD:
                    self.send_cmd(message[1])
                elif message[0] == self.GET:
                    pass
                elif message[0] == self.SET:
                    pass
                else:
                    pass
            except Exception:  # Timeout occurred
                pass  # Non-blocking wait

    def send_cmd(self,cmd):
        print(f"LidarProducer started ...")
        self.esp_connection.connect()
        self.esp_connection.send_command_packet(cmd)

    def set_param(self,paramid,value):
        pass
    def get_param(self,paramid):
        return 0


if __name__ == '__main__':
    esp_connection = ESP32PacketHandler('/dev/tty.usbserial-14440')  # Replace with your ESP32 serial port

    def test_producer():
        # Create a shared queue
        report_queue = Queue()
        cmd_queue = Queue()

        reciver_process = ESP32Reciver(report_queue,cmd_queue,esp_connection)
        reciver_process = Process(target=reciver_process.generate_data)
        reciver_process.start()

        time.sleep(3)

        commander_process = ESP32Commander(cmd_queue,esp_connection)
        commander_process = Process(target=commander_process.send_cmd)
        commander_process.start()

        print("======SAKINE=======")
        reciver_process.join()
        time.sleep(10)
        print("======SAKINE=======")

        # # Consumer simulation
        # while True:
        #     try:
        #         message = queue.get(timeout=0.001)  # 1 milliseconds timeout
        #         if message is None:  # Exit condition
        #             print("Consumer exiting.")
        #             break
        #         print(f"Consumer received: {message}")
        #     except Exception:  # Timeout occurred
        #         pass  # Non-blocking wait

    print("Starting Producer Test...")
    time.sleep(5)
    test_producer()
    print("Producer Test Finished.")
