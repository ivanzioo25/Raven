import time
import os
from sensors_Driver import scan

from notification import SendNotif
from netcheck import net_is_up
PIR = 7
Pir = "PIR"

while True:

    Sens=scan(Pir,PIR)
    #time.sleep(2)
    
    if(Sens == 1):
		netup = net_is_up()
		if(netup ==1 ):
			SendNotif("Test message")
	
