# Helpdesk Ticket Management System

A simple web-based Helpdesk Ticket Management System developed using Python, Flask, HTML, CSS and CSV for managing customer support tickets.

## Project Overview

The Helpdesk Ticket Management System helps manage customer complaints and support requests through a simple web interface.

Users can raise new tickets, assign tickets to support agents, track ticket details, view all tickets and close resolved tickets.

The application uses CSV files for permanent data storage.

## Technologies Used

- **Python** – Backend programming
- **Flask** – Web framework
- **HTML** – Frontend structure
- **CSS** – Frontend styling
- **CSV** – Data storage
- **Git & GitHub** – Version control

## Features

1. **Raise Ticket** – Create new customer support tickets.
2. **Assign Ticket** – Assign tickets to support agents.
3. **Track Ticket** – Search and view individual ticket details.
4. **View All Tickets** – Display all available tickets.
5. **Close Ticket** – Update ticket status to Closed.
6. **Dashboard** – Display total, open and closed ticket counts.
7. **Ticket History** – Maintain basic activity history for tickets.
8. **Permanent Storage** – Store ticket information in a CSV file.

## Project Structure

```text
Helpdesk_Ticket_System/
│
├── app.py
├── main.py
├── storage.py
├── ticket.py
├── raise_ticket.py
├── assign_ticket.py
├── track_ticket.py
├── view_tickets.py
├── close_ticket.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── data/
│   └── tickets.csv
│
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kaushhreddy/Helpdesk-Ticket-Management-System.git
```

### 2. Open the Project Folder

```bash
cd Helpdesk-Ticket-Management-System
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

## Data Storage

The application uses a CSV file located inside the `data` folder.

Ticket information includes:

- Ticket ID
- Customer Name
- Issue Description
- Priority
- Status
- Assigned Agent
- Created Date and Time
- Ticket History

## Future Enhancements

- User authentication and login system
- Search and filter functionality
- Improved dashboard and analytics
- Ticket status management
- Database integration
- Responsive UI improvements

## Author

**Kaushik Reddy**

B.Tech – Computer Science and Engineering (AI & ML)

---

*Developed as a beginner-friendly Python web application project.*