import RPi.GPIO as gpio
import picamera
import time
led=5
led2=6
buz=26
button=19
HIGH=1
LOW=0

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)
gpio.setup(led2, gpio.OUT)

gpio.setup(buz, gpio.OUT)
gpio.setup(button, gpio.IN)
gpio.output(led , 0)
gpio.output(buz , 0)
data=""
def capture_image():
    print("Please Wait..");
    data= time.strftime("%d_%b_%Y\%H:%M:%S")
    camera.start_preview()
    time.sleep(2)
    print ("data");
    camera.capture('/home/pi/Desktop/%s.jpg'%data)
    camera.stop_preview()
    print("Image Captured")
    print(" Successfully ")
    time.sleep(2)

print("Visitor Monitoring")
print("    Using RPI     ")
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
print(" Please Press ")
print("    Button      ")
time.sleep(2)
while 1:
    d= time.strftime("%d %b %Y")
    t= time.strftime("%H:%M:%S")
    gpio.output(led, 1)
    if gpio.input(button)==1:
        gpio.output(buz, 1)
        gpio.output(led, 0)
        time.sleep(1)
        gpio.output(buz, 0)
        print("Time: %s"%t)
        print("Date:%s"%d)
        capture_image();
        gpio.output(led2, 1)
        print("Door Open")
        time.sleep(1)
        gpio.output(led2, 0)
        print("Door Close")
    time.sleep(0.5)
