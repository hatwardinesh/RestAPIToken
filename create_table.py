import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table1 = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table1)
cursor.execute(create_table)


select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print("rows are below")
    print(row)


connection.commit()
connection.close()


