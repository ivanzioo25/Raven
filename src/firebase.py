#from usr import firebase
from firebase import firebase

firebase = firebase.FirebaseApplication('https://raven-88bf6.firebaseio.com',None)
#result = firebase.post('/ivan','caca')
result = firebase.get('/Ivan',None)
print (result)
