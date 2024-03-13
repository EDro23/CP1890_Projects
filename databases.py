import sqlite3

conn = sqlite3.connect('class_example.sqlite')

c = conn.cursor()
query = """CREATE TABLE IF NOT EXISTS students (id INTERGER PRIMARY KEY,First_Name TEXT, Last_Name TEXT, age INTEGER, marks INTEGER);"""
print(query)
c.execute(query)
print("Table created successfully")

c.execute("""INSERT INTO students VALUES (1,'Ethan', 'Drover', 23,100)""")
conn.commit()
conn.close()
