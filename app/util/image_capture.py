
import cv2
import numpy as np

def capture_image():
    # Open the camera (device index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        raise Exception("Error: Could not open video capture.")

    try:
        # Capture a single frame
        ret, frame = cap.read()

        # If the frame was captured successfully, save it
        if ret:
            cv2.imwrite("temp.jpg", frame)
        else:
            # Create a dummy image (e.g., black image)
            dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)  # Adjust dimensions as needed
            cv2.putText(dummy_image, "Dummy Image", (50, 250), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imwrite("temp.jpg", dummy_image)
    finally:
        # Release the camera and close any OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    pic = capture_image()
