from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    email: str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


@dataclass
class Customer(Person):
    customer_number: str


@dataclass
class Employee(Person):
    SSN: str


def data_entry_customer():
    print("CUSTOMER DATA ENTRY")
    firstname = input("First name: ")
    lastname = input("Last name: ")
    email = input("Email: ")
    number = input("Number: ")
    return Customer(first_name=firstname, last_name=lastname, email=email, customer_number=number)


def data_entry_employee():
    print("EMPLOYEE DATA ENTRY")
    firstname = input("First name: ")
    lastname = input("Last name: ")
    email = input("Email: ")
    ssn = input("SSN: ")
    return Employee(first_name=firstname, last_name=lastname, email=email, SSN=ssn)


def main():
    print("Customer Employee Data Entry")
    print()
    while True:
        try:
            entry = input("Customer or employee? (c/e): ")
            if entry.lower() == "c":
                customer = data_entry_customer()
                if isinstance(customer, Customer):
                    print()
                    print("Customer")
                    print(f"Name: {customer.full_name}".ljust(10))
                    print(f"Email: {customer.email}".ljust(10))
                    print(f"Number: {customer.customer_number}".ljust(10))
                    contin = input("Continue? (y/n): ")
                    if contin.lower() == 'y':
                        continue
                    else:
                        print()
                        print("Bye!")
                        break
                else:
                    print("Error: Not a Customer instance.")
            elif entry.lower() == "e":
                employee = data_entry_employee()
                if isinstance(employee, Employee):
                    print()
                    print("Employee")
                    print(f"Name: {employee.full_name}".ljust(10))
                    print(f"Email: {employee.email}".ljust(10))
                    print(f"SSN: {employee.SSN}".ljust(10))
                    contin = input("Continue? (y/n): ")
                    if contin.lower() == 'y':
                        continue
                    else:
                        print()
                        print("Bye!")
                        break
                else:
                    print("Error: Not an Employee instance.")
            else:
                print("Invalid input.")
        except ValueError:
            print("Error, Please try again.")


if __name__ == "__main__":
    main()
