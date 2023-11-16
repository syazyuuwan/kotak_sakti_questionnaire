/*Show schema generation query*/

CREATE SCHEMA kotak_test;

CREATE TABLE customers(
	id INT PRIMARY KEY,
	name VARCHAR(50),
	email VARCHAR(50),
	tel VARCHAR(15),
	created_at TIMESTAMP,
	updated_at TIMESTAMP
);

CREATE TABLE invoices(
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

CREATE TABLE invoice_lines(
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

