import cv2
import json
import requests

class WebcamCapture:
    def __init__(self, save_path: str = "captured_image.jpg"):
        self.save_path = save_path

    def capture_image(self):
        # Open the default camera (0)
        cap = cv2.VideoCapture(0)

        # Check if the camera opened successfully
        if not cap.isOpened():
            raise Exception("Error: Could not open video capture.")
        
        # Capture a single frame
        ret, frame = cap.read()

        # If the frame was captured successfully
        if ret:
            # Save the captured frame as a JPEG file
            cv2.imwrite(self.save_path, frame)
            print(f"Image saved as {self.save_path}")
        else:
            raise Exception("Error: Could not read frame.")

        # Release the camera
        cap.release()
        cv2.destroyAllWindows()

        return self.save_path

class APIClient:
    def __init__(self, api_url: str, auth_token: str):
        self.api_url = api_url
        self.auth_token = auth_token

    def send_image_with_json(self, image_path: str, json_data: dict):
        # Open the image file in binary mode
        with open(image_path, 'rb') as image_file:
            files = {'image_file': image_file}
            headers = {
                'Authorization': f'Token {self.auth_token}'
            }
            json_string = json.dumps(json_data)
            data = {
                'json': json_string
             }
            response = requests.post(self.api_url, files=files, data=data, headers=headers)

        # Check the status of the response
        if response.status_code == 201:
            print("Request successful.")
            return response.json()
        else:
            response.raise_for_status()

class ImageSender:
    def __init__(self, api_url: str, auth_token: str, barcode: str, save_path: str = "captured_image.jpg"):
        self.webcam_capture = WebcamCapture(save_path)
        self.api_client = APIClient(api_url, auth_token)
        self.barcode = barcode

    def run(self):
        # Capture image from webcam
        image_path = self.webcam_capture.capture_image()

        # JSON data to be sent
        json_data = {"barcode": self.barcode}

        # Send the image and JSON to the API
        response = self.api_client.send_image_with_json(image_path, json_data)

        # Handle the API response
        print("API Response:", response)

if __name__ == "__main__":
    # Define the API URL and Authorization Token
    api_url = "http://172.30.33.135:8000/dimension-detection/api/products/calculate-with-image/v0/"
    auth_token = "22e18ee94016891220baf146f7ef955605f40626"
    barcode = "DK-4104"
    
    # Create and run the ImageSender app
    app = ImageSender(api_url, auth_token, barcode)
    app.run()
