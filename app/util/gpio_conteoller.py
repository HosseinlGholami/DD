import RPi.GPIO as GPIO

GPIO.cleanup()

LIDAR_CTRL_GPIO = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIDAR_CTRL_GPIO,GPIO.OUT)


def lidar_controll(ctrl):
    if ctrl == True:
        GPIO.output(LIDAR_CTRL_GPIO,GPIO.HIGH)
    else:
        GPIO.output(LIDAR_CTRL_GPIO,GPIO.LOW)



if __name__ == "__main__":
    import time
    while True:
        print("HIGH")
        lidar_controll(True)
        time.sleep(3)
        print("LOW")
        lidar_controll(False)
        time.sleep(3)
        
        