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

'''

for writing any query write into query = ' write here in the following code'

code:
import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='name_of_db'
)
executor = conn.cursor()

query = """
-- query for create tables and filling data in them
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    cost DECIMAL(10, 2) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50),
    quantity INT NOT NULL,
    meal_type VARCHAR(50) -- E.g., "Kids Meal", "Regular Meal"
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    age INT NOT NULL
);

CREATE TABLE taxes (
    tax_id INT AUTO_INCREMENT PRIMARY KEY,
    tax_name VARCHAR(50) NOT NULL,
    percentage DECIMAL(5, 2) NOT NULL,
    applies_to VARCHAR(10) NOT NULL -- "Cash" or "Card"
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(10) NOT NULL, -- "Cash" or "Card"
    tax_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (tax_id) REFERENCES taxes(tax_id)
);

CREATE TABLE order_details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(10) NOT NULL, -- "Cash" or "Card"
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    meal_type VARCHAR(50),
    discount_percentage DECIMAL(5, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- filling data into them: 
-- Insert data into products
INSERT INTO products (name, description, cost, price, category, quantity, meal_type) VALUES
('Chicken Bucket', 'A bucket of crispy fried chicken', 15.00, 20.00, 'Food', 500, 'Regular Meal'),
('French Fries', 'Golden, crispy fries', 1.50, 3.00, 'Food', 800, 'Regular Meal'),
('Coke', 'Refreshing cold drink', 0.75, 1.50, 'Beverage', 1000, 'Regular Meal'),
('Chicken Sandwich', 'A sandwich with a crispy chicken fillet', 3.50, 5.00, 'Food', 600, 'Regular Meal'),
('Kids Chicken Meal', 'A meal for kids', 3.00, 4.50, 'Food', 300, 'Kids Meal'),
('Veggie Burger', 'A burger with a veggie patty', 2.50, 4.00, 'Food', 400, 'Regular Meal'),
('Onion Rings', 'Crispy fried onion rings', 2.00, 3.50, 'Food', 350, 'Regular Meal'),
('Milkshake', 'Thick, creamy milkshake', 2.50, 4.50, 'Beverage', 250, 'Regular Meal'),
('Spicy Wings', 'Wings with a spicy kick', 4.00, 6.00, 'Food', 200, 'Regular Meal'),
('Apple Pie', 'Sweet and warm apple pie', 1.50, 2.50, 'Dessert', 150, 'Regular Meal');

-- Insert data into customers
INSERT INTO customers (first_name, last_name, email, phone, address, age) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Elm Street', 30),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Oak Street', 25),
('Alice', 'Johnson', 'alice.johnson@example.com', '2345678901', '789 Pine Street', 35),
('Bob', 'Williams', 'bob.williams@example.com', '3456789012', '321 Maple Street', 28),
('Charlie', 'Brown', 'charlie.brown@example.com', '4567890123', '654 Cedar Street', 42),
('Daisy', 'Miller', 'daisy.miller@example.com', '5678901234', '987 Birch Street', 29),
('Eva', 'Davis', 'eva.davis@example.com', '6789012345', '135 Elm Street', 22),
('Frank', 'Martinez', 'frank.martinez@example.com', '7890123456', '246 Oak Street', 31),
('Grace', 'Wilson', 'grace.wilson@example.com', '8901234567', '369 Pine Street', 27),
('Hank', 'Moore', 'hank.moore@example.com', '9012345678', '481 Maple Street', 33);

-- Insert data into taxes
INSERT INTO taxes (tax_name, percentage, applies_to) VALUES
('GST', 5.00, 'Cash'),
('Card Tax', 2.00, 'Card'),
('Luxury Tax', 7.00, 'Cash'),
('Service Tax', 3.00, 'Card');

-- Insert data into discounts
INSERT INTO discounts (product_id, meal_type, discount_percentage, start_date, end_date) VALUES
(1, 'Regular Meal', 10.00, '2024-01-01', '2024-12-31'),
(2, 'Regular Meal', 5.00, '2024-06-01', '2024-12-31'),
(3, 'Regular Meal', 2.00, '2024-07-01', '2024-12-31'),
(4, 'Regular Meal', 7.00, '2024-03-01', '2024-12-31'),
(5, 'Kids Meal', 15.00, '2024-01-01', '2024-12-31');

-- Insert data into orders
INSERT INTO orders (customer_id, total_amount, payment_method, tax_id) VALUES
(1, 28.00, 'Cash', 1),
(2, 18.00, 'Card', 2),
(3, 12.00, 'Cash', 3),
(4, 30.00, 'Card', 4),
(5, 15.00, 'Cash', 1),
(6, 22.00, 'Card', 2),
(7, 25.00, 'Cash', 1),
(8, 20.00, 'Card', 4),
(9, 14.00, 'Cash', 3),
(10, 17.00, 'Card', 2);

-- Insert data into order_details
INSERT INTO order_details (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 20.00),
(1, 2, 2, 3.00),
(1, 3, 1, 1.50),
(2, 4, 2, 5.00),
(2, 5, 1, 4.50),
(3, 6, 2, 4.00),
(3, 7, 1, 3.50),
(4, 8, 1, 4.50),
(4, 9, 1, 6.00),
(5, 5, 2, 4.50),
(6, 1, 1, 20.00),
(6, 8, 1, 4.50),
(7, 3, 2, 1.50),
(7, 9, 1, 2.50),
(8, 2, 2, 3.00),
(8, 4, 1, 5.00),
(9, 1, 1, 20.00),
(9, 6, 1, 4.00),
(10, 3, 2, 1.50),
(10, 5, 1, 4.50);

-- Insert data into payments
INSERT INTO payments (order_id, payment_method, amount) VALUES
(1, 'Cash', 28.00),
(2, 'Card', 18.00),
(3, 'Cash', 12.00),
(4, 'Card', 30.00),
(5, 'Cash', 15.00),
(6, 'Card', 22.00),
(7, 'Cash', 25.00),
(8, 'Card', 20.00),
(9, 'Cash', 14.00),
(10, 'Card', 17.00);

"""

executor.execute(query)
print(executor.rowcount, "record inserted.")
executor.close()
conn.close()




some extra queries: 
 
 /*
to insert new data
INSERT INTO orders (customer_id, total_amount, payment_method, tax_id)
VALUES (1, 25.00, 'Card', 2);
INSERT INTO order_details (order_id, product_id, quantity, price, discount_percentage, tax_percentage)
VALUES (1, 2, 3, 0.00, 0.00, 0.00), (1, 4, 2, 0.00, 0.00, 0.00); 
INSERT INTO payments (order_id, payment_method, amount)
VALUES (1, 'Card', 25.00);*/

/*
-- to find total products sold
select p.name, sum(od.quantity) as quantity
from products as p
join order_details as od on p.product_id = od.product_id
group by p.name;*/

/*
-- total profit
select sum((od.price - p.cost) * od.quantity) as profit
from order_details od
join products p on od.product_id = p.product_id
*/

/*
-- finding total tax deducted
select sum(od.quantity * (od.price - (od.price / (1 + od.tax_percentage / 100)))) as total_tax
from order_details as od
*/

/*
-- customers over 15 purchasing kids meal
select count(distinct o.customer_id) as yak_customers
from orders o
join order_details od on o.order_id = od.order_id
join products p on od.product_id = p.product_id
join customers c on o.customer_id = c.customer_id
where c.age > 15 and p.meal_type = 'Kids Meal';
*/

/*
-- most famous product
select p.name, sum(od.quantity) as max
from products as p
join order_details as od on p.product_id = od.product_id
group by p.name
order by max desc limit 1*/


/*
-- Revenue by each Product
select p.name, sum(od.price)*sum(od.quantity) as revenue
from products as p
join order_details as od on p.product_id = od.product_id
group by p.name
*/


/* to quantity sold per product
select p.name, sum(od.quantity) as quantity
from products as p
join order_details as od on p.product_id = od.product_id
group by p.name*/

/*
-- total revenue generated by each payment
SELECT 
    o.payment_method, 
    SUM(od.quantity * (od.price + (od.price * (od.tax_percentage / 100)))) AS total_revenue
FROM 
    orders o
JOIN 
    order_details od ON o.order_id = od.order_id
GROUP BY 
    o.payment_method;
*/
/*
select sum(od.quantity),p.name
from order_details as od
join products as p on p.product_id= od.product_id
group by p.name
*/

/*
-- How many orders has each customer placed?
select count(od.order_id) as  no_of_oders, c.first_name
from order_details as od
join customers as c on c.customer_id= od.customer_id
group by c.first_name
*/

/*
-- Which products have had a discount applied and what are the discount percentages?
select p.name,od.discount_percentage
from products as p
join order_details as od on od.product_id=p.product_id
where discount_percentage>0.0
*/

/*
-- top 5 customers
select c.first_name,sum(o.total_amount) as spends
from orders as o
join customers as c on c.customer_id = o.customer_id
group by c.first_name
order by c.first_name desc limit 5
*/

 
 
 
 
 
 
 
 
 
 
 
 '''
