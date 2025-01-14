import json
import requests
import os
import threading
import asyncio
from queue import Queue

class APIClient:
    def __init__(self, auth_token=""):
        self.auth_token = auth_token or os.getenv("SERVER_TOKEN")
        self.image_url = "https://robotics.digikala.com/dd/api/products/calculate-with-image/v0/"
        self.lidar_url = "https://robotics.digikala.com/dd/api/products/calculate-with-point-cloud/v0/"
        self.calibration_url = "https://robotics.digikala.com/dd/api/products/camera-calibration/v0/"
        self.device_id = os.getenv("DEVICE_ID")

    def send_image(self, barcode):
        with open("temp.jpg", 'rb') as image_file:
            files = {'image_file': image_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            data = {
                'device_id': self.device_id,
                'barcode': barcode
            }
            response = requests.post(self.image_url, files=files, data=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

    def send_point_cloud(self, barcode):
        with open("temp.csv", 'rb') as csv_file:
            files = {'point_cloud_file': csv_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            data = {
                'device_id': self.device_id,
                'barcode': barcode
            }
            response = requests.post(self.lidar_url, files=files, data=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

    def camera_calibration(self):
        with open("temp.jpg", 'rb') as image_file:
            files = {'calibrate_image_file': image_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            data = {
                'device_id': self.device_id,
            }
            response = requests.post(self.calibration_url, files=files, data=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()



if __name__ == "__main__":
    import util
    barcode = "DK-013"
    auth_token = "ad9b1d5faf9a705db775f302df5d507d697b0e65"
    
    # Initialize the APIClient
    app = APIClient(auth_token)

    # Create a queue to receive results
    result_queue = Queue()

    # Run API calls asynchronously
    util.async_api_call(app, "send_point_cloud", result_queue, barcode)
    print("api is called ...")
    while True:
        try:
            result = result_queue.get(timeout=0.5)
            print("Response received:", result)
        except:
            print(".")
