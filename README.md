# kotak_sakti_questionnaire

# Answers;

### Question 1

Data Engineers build systems that collect, manage, and convert raw data into usable information for data scientists and business analysts to interpret.

Their main responsibilities include:
- Data architecture design
- Database management
- Data integration
- Data processing

### Question 2

The .sql files including the solutions are also uploaded in the repository.
Question 2.a is in [question2_schema.sql](../main/question2_schema.sql) while questions 2.b, 2.c, 2.d are in [question2_queries.sql](../main/question2_queries.sql)

#### 2.a 
```SQL
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
```

#### 2.b
```SQL
SELECT count(distinct c.name) num_customers
FROM customers c
INNER JOIN invoices i
ON c.id = i.customer_id
INNER JOIN invoice_lines il
ON i.id = il.invoice_id
HAVING sum(il.quantity)>5
;
```

#### 2.c
```SQL
SELECT c.name
FROM customers c
LEFT JOIN invoices i
on c.id = i.customer_id
WHERE i.id is null
;
```

#### 2.d
```SQL
SELECT il.description book, c.name
FROM customers c
INNER JOIN invoices i
ON c.id = i.customer_id
INNER JOIN invoice_lines il
ON i.id = il.invoice_id
;
```

### Question 3

The solution can be found in the python script [question3_python.py](../main/question3_python.py), and [queries.py](../main/queries.py) is a class that contains the queries.