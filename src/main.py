import time
import os

from notification import SendNotif
from netcheck import net_is_up

while True:
	netup = net_is_up()
	if(1 == netup):
		SendNotif("Test message")
		#time.sleep(5)
