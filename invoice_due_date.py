from datetime import datetime, timedelta


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

            # Hardcoding the due date to 30 days from the invoice date
            due_date = inv_date + timedelta(days=30)
            print("Due Date:", due_date.strftime("%B %d, %Y"))


            current_date = datetime.now()
            print("Current Date:", current_date.strftime("%B %d, %Y"))
            time_til_duedate = current_date - due_date
            print()
            print(f"The invoice is due {time_til_duedate.days} days ago.")
            print()

            contin = input("Continue? (Y/N): ")

            if contin.lower() != "y":
                break
    except ValueError:
        print("Invalid date format. Please enter the date in MM-DD-YY format.")


if __name__ == "__main__":
    main()