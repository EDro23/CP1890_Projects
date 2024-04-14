# Sales data importer program
from dataclasses import dataclass
import sqlite3
import csv



@dataclass
class Region:
    name: str = ""
    code: str = ""
    region: str = ""

    @classmethod
    def get_region_from_code(cls, code):
        conn = sqlite3.connect("Sales_data.db")
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Region WHERE code = ?''', (code,))
        row = cur.fetchone()
        conn.close()
        if row:
            return cls(name=row[1], code=row[0], region=row[2])
        else:
            return cls()  # Return an empty Region object if code is not found


@dataclass
class DailySales:
    id: int = None
    amount: int = 0
    date: str = ""
    region: Region = None
    quarter: int = 0

    @classmethod
    def from_db(cls, row):
        return cls(id=row[0], amount=row[1], date=row[2], region=Region(name=row[3], code=row[4], region=row[5]),
                   quarter=row[6])


class DB:
    @staticmethod
    def add_sales(sales):
        conn = sqlite3.connect("Sales_data.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO Sales (ID, amount, salesDate, region) VALUES (?, ?, ?, ?)''',
                    (sales.id, sales.amount, sales.date, sales.region.code))
        conn.commit()
        conn.close()

    @staticmethod
    def add_region(region):
        conn = sqlite3.connect("Sales_data.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO Region (code, name, region) VALUES (?, ?, ?)''',
                    (region.code, region.name, region.region))
        conn.commit()
        conn.close()

    @staticmethod
    def import_sales_from_csv(csv_file):
        with open(csv_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date = row['Date']
                amount = int(row['Amount'])
                region = row['Region']
                quarter = int(row['Quarter'])
                sales = DailySales(amount=amount, date=date, region=Region(name=region))
                DB.add_sales(sales)

    @staticmethod
    def get_all_sales():
        conn = sqlite3.connect("Sales_data.db")
        cur = conn.cursor()
        cur.execute('''SELECT Sales.ID, Sales.amount, Sales.salesDate, Region.name as region_name
                            FROM Sales
                            JOIN Region ON Sales.region = Region.code
                            ORDER BY date(Sales.salesDate)''')
        rows = cur.fetchall()
        return [DailySales.from_db(row) for row in rows]

    @staticmethod
    def add_imported_file(file_name):
        conn = sqlite3.connect("Sales_data.db")
        cur = conn.cursor()
        cur.execute('''INSERT INTO ImportedFiles (fileName) VALUES (?)''', (file_name,))
        conn.commit()
        conn.close()


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
    while True:
        user_input = input("Please enter command: ")
        if user_input == "view":
            sales = DB.get_all_sales()
            print("{:<2} {:<12} {:<8} {:<15} {:<15}".format("", "Date", "Quarter", "Region", "Amount"))
            print("-" * 55)
            for i, sale in enumerate(sales, start=1):
                formatted_amount = "${:,.2f}".format(sale.amount)
                print("{:<1}. {:<12} {:<8} {:<15} {:<15}".format(i, sale.date, sale.quarter, sale.region.name,
                                                                 formatted_amount))
            print("-" * 55)
        elif user_input == "add":
            amount = int(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            region_code = input("Enter region code: ")
            quarter = int(input("Enter quarter: "))
            sales = DailySales(amount=amount, date=date, region=Region.get_region_from_code(region_code),
                               quarter=quarter)
            DB.add_sales(sales)
            print("Sale added successfully.")
        elif user_input == "import":
            file_name = input("Enter CSV file name: ")
            DB.import_sales_from_csv(file_name)
            DB.add_imported_file(file_name)
            print("Imported sales successfully.")
        elif user_input == "menu":
            Menu.menu_contents()
        elif user_input == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()