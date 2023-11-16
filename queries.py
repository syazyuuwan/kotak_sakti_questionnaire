class question_queries:
    query1 = """
CREATE TABLE IF NOT EXISTS customers(
	id INT PRIMARY KEY,
	name VARCHAR(50),
	email VARCHAR(50),
	tel VARCHAR(15),
	created_at TIMESTAMP,
	updated_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS invoices(
	id INT PRIMARY KEY,
	number INT,
	sub_total DOUBLE,
	tax_total DOUBLE,
	total DOUBLE,
	customer_id INT,
	created_at TIMESTAMP,
	updated_at TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE IF NOT EXISTS invoice_lines(
	id INT PRIMARY KEY,
	description VARCHAR(20),
	unit_price DOUBLE,
	quantity INT,
	sub_total DOUBLE,
	tax_total DOUBLE,
	total DOUBLE,
	tax_id INT,
	sku_id INT,
	invoice_id INT,
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);
"""

# Show the SQL query for number of customers purchasing more than 5 books
    query2 = """
SELECT count(distinct c.name) num_customers
FROM customers c
INNER JOIN invoices i
ON c.id = i.customer_id
INNER JOIN invoice_lines il
ON i.id = il.invoice_id
HAVING sum(il.quantity)>5
;
"""

# Show the SQL query for a list of customers who never purchased anything
    query3 = """
SELECT c.name
FROM customers c
LEFT JOIN invoices i
on c.id = i.customer_id
WHERE i.id is null
;
"""

# Show the SQL query for list of book purchased with the users
    query4 = """
SELECT il.description book, c.name
FROM customers c
INNER JOIN invoices i
ON c.id = i.customer_id
INNER JOIN invoice_lines il
ON i.id = il.invoice_id
;
"""