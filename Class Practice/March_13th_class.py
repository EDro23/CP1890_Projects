import sqlite3
def create_database():

    conn = sqlite3.connect('../Programs/movies.sqlite')

    c = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS movies (id INT PRIMARY KEY, name TEXT, year INTEGER, mins INTEGER, category TEXT);"""
    c.execute(query)

def top_menu():
    print("The Movie List Program")

def menu():
    print("COMMAND MENU")
    print("cat - View movies by category")
    print("year - View movies by year")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit")

def categories():
    print("CATEGORIES")
    print("1. Animation")
    print("2. Comedy")
    print("3. History")


def add_to_database():
    conn = sqlite3.connect('../Programs/movies.db')
    movie = input(f"Name: ")
    year = input(f"Year: ")
    minutes = input(f"Minutes: ")
    categoryID = input(f"Category ID: ")

    c = conn.cursor()
    query = "INSERT INTO movies (id,name,year,mins,category) VALUES (?,?,?,?,?)"

    c.execute(query, (movie, year, int(minutes),categoryID))
    conn.commit()
    conn.close()
    print("Movie added to database")

def main():
    top_menu()
    print()
    menu()
    print()
    categories()
    print()
    create_database()
    command = input("Command: ")
    if command.lower() == 'add':
        add_to_database()


if __name__ == "__main__":
    main()

