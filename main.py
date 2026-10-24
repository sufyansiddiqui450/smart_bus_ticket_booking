# Generated from: main.ipynb
# Converted at: 2026-10-24T23:11:10.677Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

print("===================================")
print("   SMART BUS TICKET BOOKING SYSTEM")
print("===================================")
print("1. View Available Routes")
print("2. Search for a Route")
print("3. Book a Ticket")
print("4. View My Bookings")
print("5. Cancel a Booking")
print("6. View Seat Availability")
print("7. Generate Booking Report")
print("8. Exit")

# STEP 1: BUS ROUTES KA DATA

routes = [
    {
        "route_id": "R101",
        "departure_city": "Karachi",
        "destination_city": "Hyderabad",
        "departure_time": "08:00 AM",
        "ticket_price": 1200,
        "total_seats": 40,
        "available_seats": 40
    },
    {
        "route_id": "R102",
        "departure_city": "Karachi",
        "destination_city": "Sukkur",
        "departure_time": "09:30 AM",
        "ticket_price": 2000,
        "total_seats": 36,
        "available_seats": 36
    },
    {
        "route_id": "R103",
        "departure_city": "Hyderabad",
        "destination_city": "Mirpur Khas",
        "departure_time": "11:00 AM",
        "ticket_price": 800,
        "total_seats": 32,
        "available_seats": 32
    },
    {
        "route_id": "R104",
        "departure_city": "Karachi",
        "destination_city": "Lahore",
        "departure_time": "07:00 PM",
        "ticket_price": 5000,
        "total_seats": 45,
        "available_seats": 45
    },
    {
        "route_id": "R105",
        "departure_city": "Sukkur",
        "destination_city": "Hyderabad",
        "departure_time": "02:00 PM",
        "ticket_price": 1500,
        "total_seats": 30,
        "available_seats": 30
    }
]

# Supported cities
cities = (
    "Karachi", "Hyderabad", "Sukkur",
    "Mirpur Khas", "Lahore"
)

# Booking records and unique booking IDs
bookings = []
issued_booking_ids = set()
next_booking_number = 1001

print("Routes loaded successfully!")
print("Total routes:", len(routes))

# STEP 2: VIEW ROUTES

def view_routes(available_only=False):
    print("\n========== AVAILABLE BUS ROUTES ==========")
    found = False

    for number, route in enumerate(routes, start=1):
        if available_only and route["available_seats"] == 0:
            continue

        found = True

        if route["available_seats"] == 0:
            status = "Fully Booked"
        elif route["available_seats"] == route["total_seats"]:
            status = "Available"
        else:
            status = "Partially Booked"

        journey = (
            route["departure_city"] + " -> "
            + route["destination_city"]
        )

        print(f"\n{number}. Route ID: {route['route_id']}")
        print("Journey:", journey)
        print("Departure:", route["departure_time"])
        print("Fare: Rs.", route["ticket_price"])
        print(
            "Seats:",
            f"{route['available_seats']}/{route['total_seats']}"
        )
        print("Status:", status)

    if not found:
        print("No routes available.")


# STEP 2: SEARCH ROUTES

def search_route():
    search_term = input(
        "Enter route ID or departure/destination city: "
    ).strip().lower()

    if not search_term:
        print("Search input cannot be empty.")
        return

    found = False

    for route in routes:
        if search_term == route["route_id"].lower():
            print("\nRoute found:")
            print(route)
            found = True
            break

        elif (
            search_term == route["departure_city"].lower()
            or search_term == route["destination_city"].lower()
        ):
            print(
                route["route_id"], "|",
                route["departure_city"], "->",
                route["destination_city"], "|",
                "Rs.", route["ticket_price"], "|",
                route["available_seats"], "seats available"
            )
            found = True

    if not found:
        print("No matching route found.")


# Test the functions
view_routes()

search_route()

# STEP 3: BOOK A TICKET

def book_ticket():
    global next_booking_number

    print("\n========== BOOK A TICKET ==========")

    # 1. Passenger name validation
    name = input("Enter passenger name: ").strip()

    if not name:
        print("Error: Passenger name cannot be empty.")
        return

    # 2. Passenger age validation
    try:
        age = int(input("Enter passenger age: "))

        if age <= 0:
            print("Error: Age must be a positive integer.")
            return

    except ValueError:
        print("Error: Age must be a valid integer.")
        return

    # 3. Route validation
    route_id = input("Enter route ID (e.g. R101): ").strip().upper()

    selected_route = None

    for route in routes:
        if route["route_id"] == route_id:
            selected_route = route
            break

    if selected_route is None:
        print("Error: Route not found.")
        return

    # 4. Seat quantity validation
    try:
        seats = int(input("Enter number of seats: "))

        if seats <= 0:
            print("Error: Seats must be greater than zero.")
            return

    except ValueError:
        print("Error: Seat quantity must be an integer.")
        return

    # 5. Check seat availability
    if seats > selected_route["available_seats"]:
        print("Error: Not enough seats available.")
        print("Available seats:", selected_route["available_seats"])
        return

    # 6. Generate a unique booking ID
    while True:
        booking_id = f"B{next_booking_number}"
        next_booking_number += 1

        if booking_id not in issued_booking_ids:
            break

    # 7. Calculate fare
    # 7. Calculate fare and discount
    fare_per_seat = selected_route["ticket_price"]
    subtotal = fare_per_seat * seats

    if seats >= 4:
        discount_rate = 0.10
    else:
        discount_rate = 0

    discount_amount = subtotal * discount_rate
    total_fare = subtotal - discount_amount

    # 8. Create booking record
    booking = {
        "booking_id": booking_id,
        "passenger_name": name,
        "passenger_age": age,
        "route_id": route_id,
        "seats": seats,
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "total_fare": total_fare,
        "status": "Confirmed"
    }
    # 9. Save booking and update availability
    bookings.append(booking)
    issued_booking_ids.add(booking_id)
    selected_route["available_seats"] -= seats

    # 10. Confirmation
    print("\nTicket booked successfully!")
    print("Booking ID:", booking_id)
    print("Passenger:", name)
    print("Age:", age)
    print(
        "Route:",
        selected_route["departure_city"],
        "->",
        selected_route["destination_city"]
    )
    print("Seats booked:", seats)
    print("Fare per seat: Rs.", selected_route["ticket_price"])
    print("Subtotal: Rs.", subtotal)
    print("Discount: Rs.", discount_amount)
    print("Final fare: Rs.", total_fare)
    print("Status: Confirmed")
    print("Remaining seats:", selected_route["available_seats"])

book_ticket()

view_routes()

# STEP 4A: VIEW MY BOOKINGS

def view_bookings():
    print("\n========== MY BOOKINGS ==========")

    if not bookings:
        print("No bookings found.")
        return

    for number, booking in enumerate(bookings, start=1):
        print(f"\nBooking #{number}")
        print("Booking ID:", booking["booking_id"])
        print("Passenger:", booking["passenger_name"])
        print("Age:", booking["passenger_age"])
        print("Route ID:", booking["route_id"])
        print("Seats:", booking["seats"])
        print("Subtotal: Rs.", booking.get("subtotal", booking["total_fare"]))
        print("Discount: Rs.", booking.get("discount_amount", 0))
        print("Final fare: Rs.", booking["total_fare"])
        print("Status:", booking["status"])


# STEP 4B: CANCEL A BOOKING

def cancel_booking():
    print("\n========== CANCEL A BOOKING ==========")

    booking_id = input("Enter booking ID: ").strip().upper()

    selected_booking = None

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            selected_booking = booking
            break

    if selected_booking is None:
        print("Error: Booking ID not found.")
        return

    if selected_booking["status"] != "Confirmed":
        print("Error: This booking is already cancelled.")
        return

    # Find the original route
    selected_route = None

    for route in routes:
        if route["route_id"] == selected_booking["route_id"]:
            selected_route = route
            break

    if selected_route is None:
        print("Error: Original route not found.")
        return

    # Restore seats only once
    selected_route["available_seats"] += selected_booking["seats"]

    # Retain the booking record for history
    selected_booking["status"] = "Cancelled"

    print("\nBooking cancelled successfully!")
    print("Booking ID:", booking_id)
    print("Seats restored:", selected_booking["seats"])
    print("Route ID:", selected_route["route_id"])
    print("Available seats:", selected_route["available_seats"])
    print("Status: Cancelled")

view_bookings()

cancel_booking()

view_bookings()
view_routes()

# OPTION 6: VIEW SEAT AVAILABILITY

def view_seat_availability():
    print("\n========== SEAT AVAILABILITY ==========")

    if not routes:
        print("No routes found.")
        return

    for route in routes:
        available = route["available_seats"]
        total = route["total_seats"]

        if available == 0:
            status = "Fully Booked"
        elif available == total:
            status = "All Seats Available"
        else:
            status = "Partially Booked"

        print("\nRoute ID:", route["route_id"])
        print("Journey:", route["departure_city"], "->",
              route["destination_city"])
        print("Seats Available:", available)
        print("Total Seats:", total)
        print("Status:", status)


# OPTION 7: GENERATE BOOKING REPORT

def generate_booking_report():
    print("\n========== BOOKING REPORT ==========")

    total_records = len(bookings)
    confirmed_count = 0
    cancelled_count = 0
    reserved_seats = 0
    confirmed_revenue = 0
    fully_booked_routes = 0

    for booking in bookings:
        if booking["status"] == "Confirmed":
            confirmed_count += 1
            reserved_seats += booking["seats"]
            confirmed_revenue += booking["total_fare"]

        elif booking["status"] == "Cancelled":
            cancelled_count += 1

    for route in routes:
        if route["available_seats"] == 0:
            fully_booked_routes += 1

    print("Total Booking Records:", total_records)
    print("Confirmed Bookings:", confirmed_count)
    print("Cancelled Bookings:", cancelled_count)
    print("Currently Reserved Seats:", reserved_seats)
    print("Confirmed Booking Revenue: Rs.", confirmed_revenue)
    print("Fully Booked Routes:", fully_booked_routes)

    # Nested loops: show confirmed bookings route-wise
    print("\n--- Route-wise Confirmed Bookings ---")

    for route in routes:
        route_booking_found = False

        for booking in bookings:
            if (booking["route_id"] == route["route_id"]
                    and booking["status"] == "Confirmed"):
                if not route_booking_found:
                    print("\nRoute:", route["route_id"],
                          route["departure_city"], "->",
                          route["destination_city"])
                    route_booking_found = True

                print("  Passenger:", booking["passenger_name"],
                      "| Seats:", booking["seats"],
                      "| Fare: Rs.", booking["total_fare"])

        if not route_booking_found:
            print("\nRoute:", route["route_id"],
                  "- No confirmed bookings")


# ROUTE SCHEDULE GROUPED BY DEPARTURE CITY

def view_route_schedule():
    print("\n========== ROUTE SCHEDULE ==========")

    for city in cities:
        print("\nDepartures from", city, ":")
        found = False

        for route in routes:
            if route["departure_city"] == city:
                print(" ", route["route_id"], "|",
                      route["departure_city"], "->",
                      route["destination_city"], "|",
                      route["departure_time"], "| Fare: Rs.",
                      route["ticket_price"])
                found = True

        if not found:
            print("  No scheduled departures.")

view_seat_availability()

generate_booking_report()

view_route_schedule()

def main_menu():
    while True:
        print("\n======================================")
        print("  SMART BUS TICKET BOOKING SYSTEM")
        print("======================================")
        print("1. View Available Routes & Route Schedule")
        print("2. Search for a Route")
        print("3. Book a Ticket")
        print("4. View My Bookings")
        print("5. Cancel a Booking")
        print("6. View Seat Availability")
        print("7. Generate Booking Report")
        print("8. Exit")
        print("======================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            view_routes(available_only=True)
            view_route_schedule()

        elif choice == "2":
            search_route()

        elif choice == "3":
            book_ticket()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            cancel_booking()

        elif choice == "6":
            view_seat_availability()

        elif choice == "7":
            generate_booking_report()

        elif choice == "8":
            print("Thank you for using Smart Bus Ticket Booking System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 8.")


main_menu()

# Basic project checks

required_functions = [
    view_routes,
    search_route,
    book_ticket,
    view_bookings,
    cancel_booking,
    view_seat_availability,
    generate_booking_report,
    view_route_schedule
]

print("========== PROJECT CHECK ==========")

print("Total routes:", len(routes))
print("Expected routes: 5")
print("Route check:", "PASS" if len(routes) >= 5 else "FAIL")

print("Required functions:", len(required_functions))
print("Function check:", "PASS" if len(required_functions) == 8 else "FAIL")

print("Cities stored as tuple:", isinstance(cities, tuple))
print("Bookings stored as list:", isinstance(bookings, list))
print("Booking IDs stored as set:", isinstance(issued_booking_ids, set))

for route in routes:
    valid = (
        route["available_seats"] >= 0
        and route["available_seats"] <= route["total_seats"]
    )
    print(route["route_id"], ":", "PASS" if valid else "FAIL")

if __name__ == "__main__":
    main_menu()