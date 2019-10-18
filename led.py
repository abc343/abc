import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

for i in range(10):
    GPIO.output(7,True)
    print("LED ON")
    time.sleep(1)

    GPIO.output(7,False)
    print("LED OFF")
    time.sleep(1)

print("Done...")
GPIO.cleanup()
