from flask import Flask, render_template, request, redirect, url_for, flash
from storage import create_ticket_file, load_tickets, save_tickets
import datetime

app = Flask(__name__)
app.secret_key = "helpdesk123"

# Create CSV file if it does not exist
create_ticket_file()


# Home page
@app.route("/")
def home():
    tickets = load_tickets()

    total = len(tickets)
    open_tickets = 0
    closed_tickets = 0

    for ticket in tickets:
        if ticket["Status"] == "Open":
            open_tickets += 1

        if ticket["Status"] == "Closed":
            closed_tickets += 1

    return render_template(
        "index.html",
        tickets=tickets,
        total=total,
        open_tickets=open_tickets,
        closed_tickets=closed_tickets
    )


# Raise a ticket
@app.route("/raise", methods=["POST"])
def raise_ticket():

    customer = request.form["customer"]
    issue = request.form["issue"]
    priority = request.form["priority"]

    tickets = load_tickets()

    ticket_id = 1001

    for ticket in tickets:
        if ticket["ID"] >= ticket_id:
            ticket_id = ticket["ID"] + 1

    new_ticket = {
        "ID": ticket_id,
        "Customer": customer,
        "Issue": issue,
        "Priority": priority,
        "Status": "Open",
        "Assigned To": "Unassigned",
        "Created At": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "History": ["Ticket created"]
    }

    tickets.append(new_ticket)

    save_tickets(tickets)

    flash("Ticket created successfully!")

    return redirect(url_for("home"))


# Assign a ticket
@app.route("/assign", methods=["POST"])
def assign_ticket():

    entered_id = request.form["ticket_id"]
    agent = request.form["agent"]

    tickets = load_tickets()

    for ticket in tickets:
        if str(ticket["ID"]) == entered_id:

            ticket["Assigned To"] = agent

            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ticket["History"].append(time + " - Assigned to " + agent)

            save_tickets(tickets)

            flash("Ticket assigned successfully!")
            return redirect(url_for("home"))

    flash("Ticket ID not found!")
    return redirect(url_for("home"))


# Close a ticket
@app.route("/close", methods=["POST"])
def close_ticket():

    entered_id = request.form["ticket_id"]

    tickets = load_tickets()

    for ticket in tickets:
        if str(ticket["ID"]) == entered_id:

            if ticket["Status"] == "Closed":
                flash("Ticket is already closed!")
                return redirect(url_for("home"))

            ticket["Status"] = "Closed"

            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ticket["History"].append(time + " - Ticket closed")

            save_tickets(tickets)

            flash("Ticket closed successfully!")
            return redirect(url_for("home"))

    flash("Ticket ID not found!")
    return redirect(url_for("home"))


# Track a ticket
@app.route("/track", methods=["GET"])
def track_ticket():

    entered_id = request.args.get("ticket_id", "")

    tickets = load_tickets()

    selected_ticket = None

    for ticket in tickets:
        if str(ticket["ID"]) == entered_id:
            selected_ticket = ticket
            break

    return render_template(
        "index.html",
        tickets=tickets,
        total=len(tickets),
        open_tickets=sum(1 for t in tickets if t["Status"] == "Open"),
        closed_tickets=sum(1 for t in tickets if t["Status"] == "Closed"),
        selected_ticket=selected_ticket,
        search_id=entered_id
    )


if __name__ == "__main__":
    app.run(debug=True)