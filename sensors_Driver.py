import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#Select the pin distribution "BOARD" 
#-----------------------------------------------------------------------#
GPIO.setup(7, GPIO.IN)        	#Assign Pin 7 as an IN to read the PIR.
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN) 
#GPIO.setup(3, GPIO.OUT)         #LED output pin
#-----------------------------------------------------------------------#
#Pins Define:
PIR        = 7
KEY        = 11
Power_Push = 13
Key = "KEY"
Pir = "PIR"
#Power ="Power Off button"
#-----------------------------------------------------------------------#
while True:
    def scan(name,sensor):
            i=GPIO.input(sensor)
            if i==0:                 #When output from motion sensor is LOW
                print name + " " + "OFF"
                return 0
			 
            elif i==1:               #When output from motion sensor is HIGH
                print name + " " + "ON"
                return 1
				
#-----------------------------------------------------------------------#
    scan(Pir,PIR)
    if (scan(Key,KEY) == 1):
	     print "Turn off in 30s"
	     break
    time.sleep(1)	    
	
