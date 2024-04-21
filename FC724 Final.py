class SeatBookingSystem:
    def __init__(self):
        # Initialize the seating arrangement with each seat marked as 'F'(F is free)
        self.seats = {f"{i}{chr(j)}": "F" for i in range(1, 81) for j in range(65, 71)}

    def check_availability(self):
        # Check and print all available seats
        available = [seat for seat, status in self.seats.items() if status == 'F']
        print(f"Available seats: {available}")

    def book_seat(self, seat):
        # Book a seat if it is available
        if self.seats.get(seat, 'X') == 'F':  # 'X' is a fallback value if the seat does not exist
            self.seats[seat] = 'R'  # Change seat status to 'R'
            print(f"Seat {seat} booked successfully.")
        else:
            print(f"Seat {seat} is not available or does not exist.")

    def free_seat(self, seat):
        # Free a seat if it is currently booked
        if self.seats.get(seat, 'X') == 'R':  # 'X' is a fallback value if the seat does not exist
            self.seats[seat] = 'F'  # Change seat status back to 'F' 
            print(f"Seat {seat} is now free.")
        else:
            print(f"Seat {seat} was not booked or does not exist.")

    def show_booking_state(self):
        # Display the current booking state for all seats
        for seat, status in self.seats.items():
            print(f"Seat {seat}: {'Booked' if status == 'R' else 'Free'}")

    def run(self):
        # Run a continuous loop that allows the user to choose actions until they decide to exit
        while True:
            print("\n1. Check availability of seats")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.check_availability()
            elif choice == '2':
                seat = input("Enter the seat to book (e.g., 1A): ")
                self.book_seat(seat)
            elif choice == '3':
                seat = input("Enter the seat to free (e.g., 1A): ")
                self.free_seat(seat)
            elif choice == '4':
                self.show_booking_state()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Error input. Please try again.")

# Create an instance of SeatBookingSystem and run the interactive menu
system = SeatBookingSystem()
system.run()
