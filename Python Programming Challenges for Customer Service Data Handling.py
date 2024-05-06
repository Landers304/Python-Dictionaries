#Task 1:


# Initial service ticket structure
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Function to open a new service ticket
def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"New ticket {ticket_id} opened successfully for {customer_name}.")
    else:
        print("Ticket ID already exists. Please use a unique ID.")

# Function to update the status of an existing ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print("Ticket ID not found.")

# Function to display all tickets or filter by status
def display_tickets(status=None):
    if status:
        filtered_tickets = {ticket_id: ticket_details for ticket_id, ticket_details in service_tickets.items() if ticket_details["Status"] == status}
        if filtered_tickets:
            print(f"{status.capitalize()} Tickets:")
            for ticket_id, ticket_details in filtered_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer: {ticket_details['Customer']}, Issue: {ticket_details['Issue']}")
        else:
            print(f"No {status} tickets found.")
    else:
        print("All Tickets:")
        for ticket_id, ticket_details in service_tickets.items():
            print(f"Ticket ID: {ticket_id}, Customer: {ticket_details['Customer']}, Issue: {ticket_details['Issue']}, Status: {ticket_details['Status']}")

# Test the functions
open_ticket("Ticket003", "Charlie", "Technical support")
update_ticket_status("Ticket002", "open")
display_tickets("open")
