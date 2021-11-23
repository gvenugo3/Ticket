import requests
from requests.auth import HTTPBasicAuth
import json
import os

data = {}

def getData():
    loginDetails = getDetails()
    user = loginDetails[0]
    password = loginDetails[1]
    url = loginDetails[2]
    res = requests.get(url + "tickets", auth = HTTPBasicAuth(user,password))
    return res

def getDetails():
    file = open('login.json')
    data = json.load(file)
    user = data['username']
    password = data['password']
    hostname = data['hostname']
    url = "https://"+hostname+".zendesk.com/api/v2/"
    return [user,password,url]