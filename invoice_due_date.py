from datetime import datetime


def menu_top():
    print("The Invoice Due Date Program")
    print()


def main():
    menu_top()

    try:
        while True:
            inv_date_str = input("Enter the Invoice date (MM-DD-YY): ")
            inv_date = datetime.strptime(inv_date_str, "%m-%d-%y")

            print("Invoice Date:", inv_date.strftime("%B %d, %Y"))

            due_date_str = input("Enter the Due date (MM-DD-YY): ")
            due_date = datetime.strptime(due_date_str, "%m-%d-%y")
            print("Due Date:", due_date.strftime("%B %d, %Y"))

            current_date = datetime.now()
            print("Current Date:", current_date.strftime("%B %d, %Y"))
            print()
            days_between = current_date - due_date
            print(f"This invoice is {days_between.days} day(s) overdue.")

            contin = input("\nContinue? (Y/N): ")

            if contin.lower() != "y":
                break
    except ValueError:
        print("Invalid date format. Please enter the date in MM-DD-YY format.")


if __name__ == "__main__":
    main()