from raise_ticket import raise_ticket
from assign_ticket import assign_ticket
from track_ticket import track_ticket
from view_tickets import view_all_tickets
from close_ticket import close_ticket


while True:

    print("\n================================")
    print("   HELPDESK TICKET MANAGEMENT")
    print("================================")

    print("1. Raise a Ticket")
    print("2. Assign a Ticket")
    print("3. Track a Ticket")
    print("4. View All Tickets")
    print("5. Close a Ticket")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        raise_ticket()

    elif choice == "2":

        assign_ticket()

    elif choice == "3":

        track_ticket()

    elif choice == "4":

        view_all_tickets()

    elif choice == "5":

        close_ticket()

    elif choice == "6":

        print("\nThank you for using Helpdesk System!")

        break

    else:

        print("\nInvalid choice. Try again.")