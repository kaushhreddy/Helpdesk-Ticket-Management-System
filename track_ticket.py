from ticket import tickets


def track_ticket():

    print("\n--- Track Ticket ---")

    try:

        entered_id = int(input("Enter Ticket ID: "))

    except ValueError:

        print("Please enter a valid Ticket ID.")

        return

    for ticket in tickets:

        if ticket["ID"] == entered_id:

            print("\n--- Ticket Details ---")

            print("ID:", ticket["ID"])
            print("Customer:", ticket["Customer"])
            print("Issue:", ticket["Issue"])
            print("Priority:", ticket["Priority"])
            print("Status:", ticket["Status"])
            print("Assigned To:", ticket["Assigned To"])
            print("Created At:", ticket["Created At"])

            print("\n--- Ticket History ---")

            for history in ticket["History"]:

                print("-", history)

            return

    print("\nTicket ID not found.")