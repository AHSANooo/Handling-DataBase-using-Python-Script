import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password'
)

cursor = conn.cursor()
create_database_query = "Create DATABASE name_of_db"
cursor.execute(create_database_query)
cursor.close()
conn.close()
