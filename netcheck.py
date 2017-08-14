import subprocess, time

hosts = ('google.com', 'yahoo.com')

def ping(host):
  ret = subprocess.call(['ping', '-c', '3', '-W', '5', host],
    stdout=open('/dev/null', 'w'),
    stderr=open('/dev/null', 'w'))
  return ret == 0

def net_is_up():
  print "[%s] Checking network" % time.strftime("%Y-%m-%d %H:%M:%S")
  xstatus = 0

  for h in hosts:
    if ping(h):
		print "[%s] Network is up!" % time.strftime("%Y-%m-%d %H:%M:%S")
		xstatus = 1
		break
    else:
		print "[%s] Network is down!" % time.strftime("%Y-%m-%d %H:%M:%S")
		time.sleep(5)
		break
	  
		 

  #if xstatus:
    #print "[%s] Network is down :(" % time.strftime("%Y-%m-%d %H:%M:%S")

  return xstatus

#quit(net_is_up())
