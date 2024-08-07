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
-- to find total products sold
SELECT 
    p.name, SUM(od.quantity) AS quantity
FROM
    products AS p
        JOIN
    order_details AS od ON p.product_id = od.product_id
GROUP BY p.name
"""

# Executing the SQL query
cursor.execute(query)

# Fetching all results
results = cursor.fetchall()

# Closing the cursor and connection
cursor.close()
conn.close()

# Printing the results
if results:
    for row in results:
        print(f'Product: {row[0]}, Quantity Sold: {row[1]}')
else:
    print('No data found.')
