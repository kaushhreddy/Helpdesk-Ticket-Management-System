from ticket import tickets


def view_all_tickets():

    print("\n--- All Tickets ---")

    if len(tickets) == 0:

        print("No tickets available.")

    else:

        for ticket in tickets:

            print("\n-----------------------------")

            print("Ticket ID:", ticket["ID"])
            print("Customer:", ticket["Customer"])
            print("Issue:", ticket["Issue"])
            print("Priority:", ticket["Priority"])
            print("Status:", ticket["Status"])
            print("Assigned To:", ticket["Assigned To"])

            print("-----------------------------")