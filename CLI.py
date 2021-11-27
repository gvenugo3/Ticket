import API as m
from tabulate import tabulate

def CLI():
	current_page = 1
	data = { }
	try:
		data = m.getData()
	except :
		print("Connection Error")
		return "Connection Error"

	if(data == False):
		# Wrong Login Detials
		print("Error: Authentication Error")
		return "Authentication Error"

	ticket = []
	table = []
	print("\nTotal Tickets %d \n" % len(data['tickets']))
	i = 1
	for obj in data['tickets']:
		ticket.append(i)
		i += 1
		ticket.append(obj['id'])
		ticket.append(obj['subject'])
		table.append(ticket)
		ticket = []
	total_pages = len(table) // 25

	while(1):	
		Print_Table(table, current_page)
		print("\n1. Next Page (Current Page: %d, Total Pages: %d)" % (current_page, total_pages))
		print("2. Previous Page")
		print("3. Get Ticket Details")
		print("4. Exit")

		# default value is 99 if no input
		choice = int(input("Enter your choice: ") or '99')

		if(choice == 1):
			current_page += 1
			if(current_page > total_pages):
				current_page = total_pages

		elif(choice == 2):
			current_page -= 1
			if(current_page < 1):
				current_page = 1

		elif (choice == 3):
			ticket_id = input("Enter the ticket id: ")
			flag = Print_Ticket(ticket_id)
			back = 'n'
			while(back == 'n'):
				back = input("\nGo Back? (y/n)")
				if(flag == 0 or flag == 1):
					break


		elif(choice == 4):
			break

# Function to print the ticket list in pages
def Print_Table(table, page):
	size = len(table)
	total_pages = size // 25
	headers = ["#","Ticket ID","Subject"]
	if(page == total_pages):
		print(tabulate(table[(page - 1) * 25 : ], headers, tablefmt="github"))
		return 0

	print(tabulate(table[(page - 1) * 25 : page * 25], headers, tablefmt="github"))
	return 1

# Function to print details of ticket 'ticker_id'
def Print_Ticket(ticket_id):
	ticket = m.getTicket(ticket_id)

	if(ticket == 1):
		print("Authentication Error")
		return 0
	
	if(ticket == 0):
		print('Error: Ticket not Found')
		return 0

	ticket = ticket['ticket']
	print("\nSubject - %s" % ticket['subject'])
	print('\nDescription - %s' % ticket['description'])
	print("\nStatus - %s" % ticket['status'])

CLI()
	