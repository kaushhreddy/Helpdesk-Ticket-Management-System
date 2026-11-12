import datetime

from ticket import tickets
from storage import save_tickets


def assign_ticket():

    print("\n--- Assign Ticket ---")

    try:

        entered_id = int(input("Enter Ticket ID: "))

    except ValueError:

        print("Please enter a valid Ticket ID.")

        return

    agent = input("Enter Agent Name: ")

    for ticket in tickets:

        if ticket["ID"] == entered_id:

            ticket["Assigned To"] = agent

            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ticket["History"].append(
                time + " - Assigned to " + agent
            )

            save_tickets(tickets)

            print("\nTicket assigned successfully!")

            return

    print("\nTicket ID not found.")