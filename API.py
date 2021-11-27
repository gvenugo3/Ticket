import requests
from requests.auth import HTTPBasicAuth
import json

# Function to retrieve list of all tickets
def getData():
	loginDetails = getDetails()
	user = loginDetails[0]
	password = loginDetails[1]
	url = loginDetails[2]
	res = requests.get(url + "tickets", auth = HTTPBasicAuth(user,password))

	if(res.status_code >= 400):
		return False

	return res.json()

# Function to retrieve details of ticket with Ticket ID 'ticketId'
def getTicket(ticketId):
	loginDetails = getDetails()
	user = loginDetails[0]
	password = loginDetails[1]
	url = loginDetails[2]
	res = requests.get(url + "tickets/" + str(ticketId) + ".json", auth = HTTPBasicAuth(user,password))
	
	if(res.status_code >= 400 and 'error' in res.json()):
		return 0
	elif (res.status_code >= 400):
		return 1

	return res.json()

# Reads login.json for user auth details
def getDetails():
	try:
		file = open('login.json')
	except:
		print("Login Details not found. login.json file not found")
		return -1
	data = json.load(file)
	user = data['username']
	password = data['password']
	hostname = data['hostname']
	url = "https://"+hostname+".zendesk.com/api/v2/"
	return [user,password,url]