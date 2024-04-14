# Sales data importer program
from dataclasses import dataclass
import csv
from datetime import datetime


@dataclass
class Region:
    name: str = ""
    code: str = ""
    region: str = ""

    @classmethod
    def get_region_from_code(cls, code):
        for region in Region.__subclasses__():
            if region.code == code:
                return region

    @classmethod
    def valid_codes(cls, code):
        for region in Region.__subclasses__():
            if region.code == code:
                yield region


@dataclass
class File:
    def __init__(self):
        pass

    filename: str = ""
    region: Region = None

    @classmethod
    def get_region_from_filename(cls, filename):
        for region in Region.__subclasses__():
            if region.code == filename.code:
                return region

    @classmethod
    def valid_filename(cls, filename):
        for region in Region.__subclasses__():
            if region.code == filename.code:
                return region
            else:
                if filename.code == region.code:
                    return region


@dataclass
class DailySales:
    amount: int = 0
    date: str = ""
    region: Region = None
    quarter: int = 0

    def __post_init__(self):
        self.quarter = self.calculate_quarter()

    def calculate_quarter(self):
        # Convert the date string to a datetime object
        try:
            date_obj = datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Expected format: YYYY-MM-DD")
            return 0
        # Determine the quarter based on the month of the date
        quarter = (date_obj.month - 1) // 3 + 1
        return quarter

    @classmethod
    def save_to_csv(cls, csv_file):
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Date', 'Amount', 'Region', 'Quarter'])

    @classmethod
    def valid_data(cls, csv_file):
        try:
            with open(csv_file, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        date = row['Date']
                        amount = int(row['Amount'])
                        region = row['Region']
                        quarter = int(row['Quarter'])
                        yield DailySales(amount=amount, date=date, region=Region(name=region), quarter=quarter)
                    except ValueError as e:
                        print(f"Error processing data: {e}. Skipping this entry.")
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")

    @classmethod
    def valid_data(cls, csv_file):
        with open(csv_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    date = row['Date']
                    amount = int(row['Amount'])
                    region = row['Region']
                    quarter = int(row['Quarter'])
                    yield date, amount, region, quarter
                except ValueError as e:
                    print(f"Error processing data: {e}. Skipping this entry.")


class SalesList:
    sales_data = []

    @classmethod
    def add_daily_sales_to_list(cls, sales):
        cls.sales_data.append(sales)

    @classmethod
    def view_daily_sales(cls):
        total_amount = 0
        print("{:<2} {:<12} {:<8} {:<15} {:<15}".format("", "Date", "Quarter", "Region", "Amount"))
        print("-" * 55)
        for i, sale in enumerate(cls.sales_data, start=1):
            amount = int(sale.amount)  # Convert sale.amount to an integer
            total_amount += amount
            formatted_amount = "${:,.2f}".format(amount)
            print("{:<1}. {:<12} {:<8} {:<15} {:<15}".format(i, sale.date, sale.quarter, sale.region.name,
                                                             formatted_amount))
        print("-" * 55)
        formatted_total = "${:,.2f}".format(total_amount)
        print("{:<3} {:<12} {:<8} {:<15} {:<15}".format("Total", "", "", "", formatted_total))

    @classmethod
    def add_contents_to_daily_sales(cls, csv_file):
        for data in DailySales.valid_data(csv_file):
            sale = DailySales(amount=data[1], date=data[0], region=Region(name=data[2]), quarter=data[3])
            cls.add_daily_sales_to_list(sale)


class Menu:
    @staticmethod
    def menu_contents():
        print("COMMAND MENU")
        print("view - View all sales")
        print("add - Add sales")
        print("import - Import sales from CSV file")
        print("menu - Show menu")
        print("exit - Exit the program")
        print()


def main():
    print("SALES DATA IMPORTER")
    print()
    Menu.menu_contents()
    sales_list = SalesList()  # Create an instance of SalesList
    while True:
        user_input = input("Please enter command: ")
        if user_input == "view":
            sales_list.view_daily_sales()  # Call instance method on the sales_list instance
        elif user_input == "add":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = input("Enter amount: ")
            try:
                amount = int(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid integer amount.")
                continue
            region = input("Enter region: ")
            sale = DailySales(amount=amount, date=date, region=Region(name=region))
            sales_list.add_daily_sales_to_list(sale)  # Add the sale to the sales list
            print("Sale added successfully.")
        elif user_input == "import":
            file_name = input("Enter CSV file name: ")
            sales_list.add_contents_to_daily_sales(file_name)  # Call instance method on the sales_list instance
            print("Added sales successfully.")
        elif user_input == "menu":
            Menu.menu_contents()
        elif user_input == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()