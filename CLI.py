import Main as m
from tabulate import tabulate

def CLI():
	current_page = 1
	data = m.getData()
	if(data == false):
		print("Error: Authentication Error")
		return
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
		choice = int(input("Enter your choice: "))

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
			Print_Ticket(ticket_id)
			back = 'n'
			while(back == 'n'):
				back = input("\nGo Back? (y/n)")


		elif(choice == 4):
			break
		print(choice)

def Print_Table(table, page):
	size = len(table)
	total_pages = size // 25
	headers = ["#","Ticket ID","Subject"]
	if(page == total_pages):
		print(tabulate(table[(page - 1) * 25 : ], headers, tablefmt="github"))
		return

	print(tabulate(table[(page - 1) * 25 : page * 25], headers, tablefmt="github"))

def Print_Ticket(ticket_id):
	ticket = m.getTicket(ticket_id)
	ticket = ticket['ticket']
	print(ticket['id'])
	if('error' in ticket):
		print('Error: Ticket not Found')
		return 0
	
	table = []
	details = []
	details.append(ticket['id'])
	details.append(ticket["subject"])
	details.append(ticket["description"])
	details.append(ticket["status"])
	table.append(details)
	header = ['ID',"Subject","Description","Status"]
	print(tabulate(table, header, tablefmt="github"))
	

CLI()