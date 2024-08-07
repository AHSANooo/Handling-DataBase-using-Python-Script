import mysql.connector

# Establishing the connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',      # e.g., 'localhost'
    user='root',  # e.g., 'root'
    password='687354@@',
    database='kfc_management'  # e.g., 'kfc_management_system'
)

# Creating a cursor object using the connection
cursor = conn.cursor()

# Defining the SQL query to calculate the total profit
query = """
SELECT SUM((od.price - p.cost) * od.quantity) AS profit
FROM order_details od
JOIN products p ON od.product_id = p.product_id;
"""

# Executing the SQL query
cursor.execute(query)

# Fetching the result
result = cursor.fetchone()

# Closing the cursor and connection
cursor.close()
conn.close()

# Printing the result
if result:
    print(f'Total Profit: {result[0]}')
else:
    print('No data found.')
