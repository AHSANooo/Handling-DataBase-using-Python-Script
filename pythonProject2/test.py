import mysql.connector

# Creating a connection object
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="687354@@", database='kfc_management')

# printing the connection object
print(conn_obj)
cursor = conn_obj.cursor()

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
