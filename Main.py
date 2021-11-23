from fastapi import FastAPI
import requests
from requests.auth import HTTPBasicAuth
import json
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

data = {}

@app.get("/tickets")
def get_tickets():
    res = getData()
    return res.json()

def getData():
    loginDetails = getDetails()
    user = loginDetails[0]
    password = loginDetails[1]
    url = loginDetails[2]
    res = requests.get(url + "tickets", auth = HTTPBasicAuth(user,password))
    return res
