import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

if __name__ == "__main__":
    import time
    while True:
        print("HIGH")
        GPIO.output(22,GPIO.HIGH)
        time.sleep(3)
        print("LOW")
        GPIO.output(22,GPIO.LOW)
        time.sleep(3)
        
        