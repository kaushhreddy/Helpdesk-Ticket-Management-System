from ticket import create_ticket


def raise_ticket():

    print("\n--- Raise New Ticket ---")

    customer = input("Enter Customer Name: ")

    issue = input("Enter Issue: ")

    print("\nSelect Priority")

    print("1. Low")
    print("2. Medium")
    print("3. High")
    print("4. Urgent")

    choice = input("Enter Priority: ")

    priorities = {
        "1": "Low",
        "2": "Medium",
        "3": "High",
        "4": "Urgent"
    }

    if choice not in priorities:

        print("Invalid priority!")

        return

    priority = priorities[choice]

    create_ticket(customer, issue, priority)