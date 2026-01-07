-- Total revenue from all transactions
SELECT sum(p.single_price * t.amount) AS total_revenue
FROM 
	transaction t
JOIN 
	product p ON t.product_id = p.id;


-- Total spent by each customer
SELECT 
	c.id AS customer_id,
	c.firstname,
	c.lastname,
	SUM(p.single_price * t.amount) AS total_spent
FROM 
	customer c
JOIN 
	"order" o ON c.id = o.customer_id
JOIN 
	transaction t ON o.id = t.order_id
JOIN 
	product p ON t.product_id = p.id
GROUP BY 
	c.id,
	c.firstname,
	c.lastname
ORDER BY 
	total_spent DESC;


-- Count of orders by processing status
SELECT 
	ps.status_name,
	COUNT(o.id) AS order_count
FROM 
	processing_status ps
LEFT JOIN 
	"order" o ON ps.id = o.status_id
GROUP BY 
	ps.status_name;


-- Count of sold products and total spent by category
SELECT
	p.category,
	SUM(t.amount) as total_sellings
	SUM(p.single_price * t.amount) AS spent
FROM
	transaction t
JOIN
	product p ON t.product_id = p.id
GROUP BY
	p.category;


-- Count of sold products and total spent by date
SELECT
	o.order_date::date as order_date,
	SUM(t.amount) as sold,
	SUM(p.single_price * t.amount) AS spent
FROM
	transaction t
JOIN
	"order" o ON t.order_id = o.id
JOIN
	product p ON t.product_id = p.id
GROUP BY
	o.order_date;
