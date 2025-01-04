import json , requests , os


class APIClient:
    def __init__(self,auth_token):
        if auth_token:
            self.auth_token = auth_token
        else:
            self.auth_token =  os.getenv("SERVER_TOKEN")
        self.image_url       =  "https://robotics.digikala.com/dd/api/products/calculate-with-image/v0/"
        self.lidar_url       =  "https://robotics.digikala.com/dd/api/products/calculate-with-point-cloud/v0/"
        self.calibration_url =  "https://robotics.digikala.com/dd/api/products/camera-calibration/v0/"


    def send_image(self,barcode,device_id):
        # Open the image file in binary mode
        with open("temp.jpg", 'rb') as image_file:
            files = {'image_file': image_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            data = {
                'device_id': device_id,
                'barcode': barcode
             }
            response = requests.post(self.image_url, files=files, data=data, headers=headers)

        # Check the status of the response
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()

    def send_point_cloud(self,barcode,device_id):
        # Open the image file in binary mode
        with open("temp.csv", 'rb') as csv_file:
            files = {'point_cloud_file': csv_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            data = {
                'device_id': device_id,
                'barcode': barcode
             }
            response = requests.post(self.lidar_url, files=files, data=data, headers=headers)

        # Check the status of the response
        if response.status_code == 201:
            return response.json()
        else:
            print(response.json())
            response.raise_for_status()


    def camera_calibration(self,barcode,device_id):
        # Open the image file in binary mode
        with open("temp.jpg", 'rb') as image_file:
            files = {'calibrate_image_file': image_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            data = {
                'device_id': device_id,
                'barcode': barcode
             }
            response = requests.post(self.image_url, files=files, data=data, headers=headers)

        # Check the status of the response
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()



if __name__ == "__main__":
    # Define the API URL and Authorization Token
    barcode = "DK-013"
    auth_token="ad9b1d5faf9a705db775f302df5d507d697b0e65"
    # Create and run the ImageSender app
    app = APIClient(auth_token)
    # a= app.send_image_with_json(barcode,1)
    # print(a)
    # a= app.send_point_cloud(barcode,1)
    # print(a)

    