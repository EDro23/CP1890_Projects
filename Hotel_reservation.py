from Hotel_reservation_classes import HotelReservation
from datetime import datetime

def program_top():
    print("The hotel reservation program")
    print()

def main():
    while True:
        try:
            arrival_str = input("Enter arrival date (YYYY-MM-DD): ")
            departure_str = input("Enter departure date (YYYY-MM-DD): ")

            arrival = datetime.strptime(arrival_str, "%B-%d-%M")
            departure = datetime.strptime(departure_str, "%Y-%m-%d")

            if arrival >= departure:
                print("Incorrect arrival date")
            else:
                arrival = datetime.strptime("{%B} {%d}, {%M}".format(arrival))
                print(f"Arrival date: {arrival}")
                # Continue with the rest of your program

        except ValueError:
            print("Invalid date format. Please enter dates in the format YYYY-MM-DD.")

if __name__ == "__main__":
    main()