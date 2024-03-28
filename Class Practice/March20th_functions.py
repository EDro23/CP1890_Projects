import sqlite3
from March20th_databaseprac import Category, Movie

DB_FILE = '../Programs/movies.sqlite'


def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def close(conn):
    conn.close()
    print('Database closed')


def create_table(conn):
    cursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS categories ( id INTEGER PRIMARY KEY, name TEXT)"
    cursor.execute(query)
    conn.commit()
    query = 'CREATE TABLE IF NOT EXISTS movies ( name TEXT PRIMARY KEY, year INTEGER, minutes INTEGER, category INTEGER)'
    cursor.execute(query)
    conn.commit()
    print("Tables created successfully")

def create_catergory_entries(conn):
    cursor = conn.cursor()
    query = "INSERT INTO categories VALUES (?, ?)"
    category_collection = ((1, 'Animation'), (2, 'Comedy'), (3, 'History'))
    for i in range(len(category_collection)):
        cursor.execute(query, category_collection[i])
    conn.commit()
    print("Category entries inserted successfully into categories")


def get_categories(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_category_id(conn, category_name):
    cursor = conn.cursor()
    query = f"SELECT id FROM categories WHERE name = '{category_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def get_category_name(conn, category_name):
    cursor = conn.cursor()
    query = f"SELECT name FROM categories WHERE id = '{category_id}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def make_category_object(conn, row):
    category_name = get_category_name(conn, id)
    return Category(id, category_name)

def create_movie_entries(conn):
    cursor = conn.cursor()
    query = 'INSERT INTO movies VALUES (?,?,?,?)'
    movie_collection = (('Spirited away', 2005, 125, get_category_id(conn, 'Spirited away')))

if __name__ == '__main__':
    conn = connect()
    create_table(conn)
    #create_catergory_entries(conn)
    for category in get_categories(conn):
        print(category['id'], category['name'])
        print(get_category_id(conn, 'Comedy'))
        print(get_category_name(conn, 'Comedy'))
    close(conn)
