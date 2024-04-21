import random
import string

class SeatBookingSystem:
    def __init__(self):
        # Initialize each seat as 'Free' ('F') and without any booking details.
        # The seats are arranged from 1 to 80 and columns from A to F.
        self.seats = {f"{i}{chr(j)}": {'status': 'F', 'booking_info': None} for i in range(1, 81) for j in range(65, 71)}

    def generate_booking_reference(self):
        """Generate a unique booking reference of exactly eight alphanumeric characters."""
        while True:
            # Create a random string of 8 alphanumeric characters.
            reference = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            # Ensure the reference is unique by checking against all existing bookings.
            if all(reference != info['booking_info']['reference'] for seat, info in self.seats.items() if info['booking_info']):
                return reference  # Return the unique reference.

    def book_seat(self, seat, first_name, last_name, passport_number):
        """Book a seat with provided customer details if it is free."""
        # Check if the seat is free before booking.
        if self.seats.get(seat, {}).get('status') == 'F':
            # Generate a unique booking reference.
            reference = self.generate_booking_reference()
            # Store booking details in the seat's dictionary.
            self.seats[seat] = {
                'status': 'R',  # Mark the seat as reserved.
                'booking_info': {
                    'reference': reference,
                    'first_name': first_name,
                    'last_name': last_name,
                    'passport_number': passport_number
                }
            }
            print(f"Seat {seat} booked successfully with reference {reference}.")
        else:
            print(f"Seat {seat} is not available or does not exist.")

    def free_seat(self, seat):
        """Free a seat and remove all associated booking details."""
        # Check if the seat is currently reserved before freeing it.
        if self.seats.get(seat, {}).get('status') == 'R':
            # Reset the seat to free and clear booking details.
            self.seats[seat] = {'status': 'F', 'booking_info': None}
            print(f"Seat {seat} is now free.")
        else:
            print(f"Seat {seat} was not booked or does not exist.")

    def show_booking_state(self):
        """Display the current booking state for all seats."""
        # Loop through all seats to display their current booking status.
        for seat, info in self.seats.items():
            status = 'Booked' if info['status'] == 'R' else 'Free'
            print(f"Seat {seat}: {status}")

    def run(self):
        """Run the interactive command menu for the seat booking system."""
        while True:
            print("\n1. Check availability of seats")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            choice = input("Enter your choice: ")

            # Handle user input to perform actions based on the choice made.
            if choice == '1':
                self.show_booking_state()
            elif choice == '2':
                seat = input("Enter the seat to book (e.g., 1A): ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                passport_number = input("Enter passport number: ")
                self.book_seat(seat, first_name, last_name, passport_number)
            elif choice == '3':
                seat = input("Enter the seat to free (e.g., 1A): ")
                self.free_seat(seat)
            elif choice == '4':
                self.show_booking_state()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid input. Please try again.")

# Example usage:
system = SeatBookingSystem()
system.run()
