import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SENSOR_PIN = 10

GPIO.setup(SENSOR_PIN, GPIO.IN)

print("IR Sensor has started")
print("Press Cntrl+C to stop")

try:
        while True:
                if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
                        print("Object detected")
                else:
                        print("No object")
                time.sleep(0.1)

except KeyboardInterrupt:
        print("\nExiting program")

finally:
        GPIO.cleanup()