/*Show the SQL query for number of customers purchasing more than 5 books*/

select count(distinct c.name) num_customers
from customers c
inner join invoices i
on c.id = i.customer_id
inner join invoice_lines il
on i.id = il.invoice_id
having sum(il.quantity)>5
;

/*Show the SQL query for a list of customers who never purchased anything*/

select c.name
from customers c
left join invoices i
on c.id = i.customer_id
where i.id is null
;

/*Show the SQL query for list of book purchased with the users*/

select il.description book, c.name
from customers c
inner join invoices i
on c.id = i.customer_id
inner join invoice_lines il
on i.id = il.invoice_id
;