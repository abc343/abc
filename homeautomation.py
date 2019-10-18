import RPi.GPIO as GPIO import time import string 
RelayPin = 17 
def setup():
    GPIO.setwarnings(False)
    set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set RelayPin's mode to output,and initial level to LOW(0V)
    GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.HIGH) 
def ledon():
    GPIO.output(RelayPin,GPIO.LOW) 
def ledoff():
    GPIO.output(RelayPin,GPIO.HIGH) 
def main():
    while 1:
        c=input("Enter your choice(ON/OFF/TERMINATE):   ")
        l=c.lower()
        if l=="on":
            ledon()
        elif l=="off":
            ledoff()
        elif l=="terminate":
            destroy()
            break
        else:
            print("Enter valid input")   
def destroy():
    #turn off relay
    GPIO.output(RelayPin,GPIO.HIGH)
    #release resource
    GPIO.cleanup() 
if __name__ == '__main__':
    setup()
    main() 
