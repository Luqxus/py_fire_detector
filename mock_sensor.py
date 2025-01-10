import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17  # Virtual pin

GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(SENSOR_PIN):
            print("Sensor triggered!")
        else:
            print("Sensor idle.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program stopped.")
finally:
    GPIO.cleanup()