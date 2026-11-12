import csv
import os

# Create data folder
if not os.path.exists("data"):
    os.makedirs("data")


# CSV file location
file = "data/tickets.csv"


# Column names
columns = [
    "ID",
    "Customer",
    "Issue",
    "Priority",
    "Status",
    "Assigned To",
    "Created At",
    "History"
]


# Create CSV file
def create_ticket_file():

    if not os.path.exists(file):

        with open(file, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(columns)

        print("Ticket storage created successfully!")


# Read all tickets
def load_tickets():

    tickets = []

    with open(file, "r", newline="") as f:

        reader = csv.DictReader(f)

        for ticket in reader:

            ticket["ID"] = int(ticket["ID"])

            if ticket["History"]:
                ticket["History"] = ticket["History"].split("|")
            else:
                ticket["History"] = []

            tickets.append(ticket)

    return tickets


# Save all tickets
def save_tickets(tickets):

    with open(file, "w", newline="") as f:

        writer = csv.DictWriter(f, fieldnames=columns)

        writer.writeheader()

        for ticket in tickets:

            new_ticket = ticket.copy()

            new_ticket["History"] = "|".join(ticket["History"])

            writer.writerow(new_ticket)