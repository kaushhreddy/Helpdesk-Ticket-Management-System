import datetime

from ticket import tickets
from storage import save_tickets


def close_ticket():

    print("\n--- Close Ticket ---")

    try:

        entered_id = int(input("Enter Ticket ID: "))

    except ValueError:

        print("Please enter a valid Ticket ID.")

        return

    for ticket in tickets:

        if ticket["ID"] == entered_id:

            if ticket["Status"] == "Closed":

                print("\nTicket is already closed!")

                return

            ticket["Status"] = "Closed"

            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ticket["History"].append(
                time + " - Ticket closed"
            )

            save_tickets(tickets)

            print("\nTicket closed successfully!")

            return

    print("\nTicket ID not found.")