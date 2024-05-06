#Task 1:


# Initial hotel room structure
hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

# Function to book a room
def book_room(room_number, customer_name):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} booked successfully for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")

# Function to check-out a customer
def checkout_customer(room_number):
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"Checked out {customer_name} from Room {room_number}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")

# Function to display the status of all rooms
def display_room_status():
    print("Room Status:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: {details['status'].capitalize()} by {details['customer']}")

# Test the functions
book_room("103", "Alice")
checkout_customer("102")
display_room_status()
