import datetime

from storage import create_ticket_file, load_tickets, save_tickets


# Create CSV file if it doesn't exist
create_ticket_file()


# Load previously saved tickets
tickets = load_tickets()


# Generate the next ticket ID
ticket_id = 1001

for ticket in tickets:

    if ticket["ID"] >= ticket_id:

        ticket_id = ticket["ID"] + 1


# Create a new ticket
def create_ticket(customer, issue, priority):

    global ticket_id

    ticket = {
        "ID": ticket_id,
        "Customer": customer,
        "Issue": issue,
        "Priority": priority,
        "Status": "Open",
        "Assigned To": "Unassigned",
        "Created At": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "History": ["Ticket created"]
    }

    # Add ticket to the list
    tickets.append(ticket)

    # Save tickets permanently
    save_tickets(tickets)

    print("\nTicket created successfully!")

    print("Ticket ID:", ticket_id)

    ticket_id = ticket_id + 1