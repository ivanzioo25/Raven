import RPi.GPIO as GPIO
import time
import os
#import Send_Message.py

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		#Select the pin distribution "BOARD" 
#-----------------------------------------------------------------------#
GPIO.setup(7, GPIO.IN)        	#Assign Pin 7 as an IN to read the PIR.
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN) 
#GPIO.setup(3, GPIO.IN)         #POWER button
#-----------------------------------------------------------------------#
#Pins Define:

#Power ="Power Off button"
#-----------------------------------------------------------------------#

def scan(name,sensor):
           
            i=GPIO.input(sensor)
            if i==0:                 #When output from motion sensor is LOW
                print name + " " + "OFF"
                return 0
			 
            elif i==1:               #When output from motion sensor is HIGH
                print name + " " + "ON"
                #os.system("python Send_Message.py")
                #time.sleep(3)
                return 1
				
#-----------------------------------------------------------------------#
   # scan(Pir,PIR)
    #if (scan(Key,KEY) == 1):
	 #    print "Turn off in 30s"
	  #   os.system("sudo shutdown -h -t 1")
	   #  break
        
#    elif(scan(Power,Power_Push) == 1):
#         os.system("sudo shutdown -h now")
    #time.sleep(1)	    
	
