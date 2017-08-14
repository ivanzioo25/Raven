import pycurl, json
import os
import time
from StringIO import StringIO
from netcheck import net_is_up

#setup InstaPush variables
# add your Instapush Application ID
appID = "593421a7a4c48a4298b5f553"

# add your Instapush Application Secret
appSecret = "f0d03205f40f692dc3e67da8ac215599"
pushEvent = "Alarm"

def SendNotif(message):
	#Get the message
	pushMessage = message
	
	# use this to capture the response from our push API call
	buffer = StringIO()

	# use Curl to post to the Instapush API
	c = pycurl.Curl()

	# set API URL
	c.setopt(c.URL, 'https://api.instapush.im/v1/post')

	#setup custom headers for authentication variables and content type
	c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
				'x-instapush-appsecret: ' + appSecret,
				'Content-Type: application/json'])

	# create a dict structure for the JSON data to post
	json_fields = {}

	# setup JSON values
	json_fields['event']=pushEvent
	json_fields['trackers'] = {}
	json_fields['trackers']['message']=pushMessage
	#print(json_fields)
	postfields = json.dumps(json_fields)

	# make sure to send the JSON with post
	c.setopt(c.POSTFIELDS, postfields)

	# set this so we can capture the resposne in our buffer
	c.setopt(c.WRITEFUNCTION, buffer.write)

	# uncomment to see the post sent
	#c.setopt(c.VERBOSE, True)

	# in the door is opened, send the push request
	try:
		c.perform()
	except:
		print "[%s] Network is down" % time.strftime("%Y-%m-%d %H:%M:%S")
		print "[%s] Restart main.py" % time.strftime("%Y-%m-%d %H:%M:%S")
		os.system("python main.py")

	# capture the response from the server
	body= buffer.getvalue()

	# print the response
	print(body)

	# reset the buffer
	buffer.truncate(0)
	buffer.seek(0)

	# cleanup
	c.close()
	
#quit(SendNotif("caca"))

