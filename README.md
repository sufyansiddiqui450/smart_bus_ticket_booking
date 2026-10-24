# Smart Bus Ticket Booking & Reservation System

## Project Overview
This beginner-friendly Python console application lets users view and search bus routes, book tickets, view bookings, cancel bookings, check seat availability, generate a booking report, and view the route schedule.

## Requirements
- Python 3
- Anaconda Jupyter Notebook or another Python 3 environment
- No third-party Python libraries required

## Features
1. View available bus routes
2. Search for a route by route ID or city
3. Book a ticket with passenger and seat validation
4. View booking records
5. Cancel a confirmed booking and restore seats once
6. View seat availability
7. Generate a booking report
8. View route schedule grouped by departure city
9. Exit the application

Note: The current menu has nine numbered choices because route schedule was added as an extra option. If the project brief requires exactly eight menu options, combine the route schedule with another option or adjust the menu before submission.

## Sample Routes
- R101: Karachi to Hyderabad — 08:00 AM — Rs. 1,200 — 40 seats
- R102: Karachi to Sukkur — 09:30 AM — Rs. 2,000 — 36 seats
- R103: Hyderabad to Mirpur Khas — 11:00 AM — Rs. 800 — 32 seats
- R104: Karachi to Lahore — 07:00 PM — Rs. 5,000 — 45 seats
- R105: Sukkur to Hyderabad — 02:00 PM — Rs. 1,500 — 30 seats

## How to Run in Anaconda Jupyter Notebook
1. Open Anaconda Jupyter Notebook.
2. Create a new Python notebook.
3. Paste the code cells in order: data setup, route functions, booking, booking viewing/cancellation, seat availability/report/schedule, and main menu.
4. Run each cell from top to bottom.
5. Use the displayed menu to test the application.

Run the cell containing `main_menu()` only after all data and function cells have run.

## Booking Rules
- Passenger name cannot be blank.
- Age must be a positive integer.
- The route ID must exist.
- Seat quantity must be a positive integer.
- Requested seats cannot exceed available seats.
- Fare = ticket price multiplied by seats booked.
- Cancelled bookings remain in the records with status `Cancelled`.
- Seats are restored only when a confirmed booking is cancelled for the first time.
- Reports count revenue and reserved seats from confirmed bookings only.

## Data Storage and Limitations
- Routes and bookings are stored in Python lists and dictionaries while the program runs.
- Booking IDs are tracked in a set to avoid reuse during the current run.
- Data is stored in memory only and is lost when the program or notebook kernel is restarted.
- This is a console application, not a website, mobile app, or database-backed system.

## Testing
Use `test_cases.txt` for manual testing. Record actual results and mark each test PASS or FAIL during final verification.

## Submission Checklist
- [ ] Python source file (`main.py`) or complete notebook (`.ipynb`)
- [ ] `README.md`
- [ ] `test_cases.txt` with actual PASS/FAIL results
- [ ] Screenshot of route listing
- [ ] Screenshot of successful booking
- [ ] Screenshot of successful cancellation
- [ ] Screenshot of booking report
- [ ] Short demonstration and explanation
