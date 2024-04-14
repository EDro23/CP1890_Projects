import sqlite3

# This is for clearing the data of the tables. I also provided the CSV so you can import it again.
# To whom ever this may concern
def clear_sales_table():
    conn = sqlite3.connect("Sales_data.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Sales")
    cur.execute("DELETE FROM ImportedFiles")
    conn.commit()
    conn.close()

# Call the function to clear the Sales table
clear_sales_table()