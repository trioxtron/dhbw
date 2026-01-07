CREATE TABLE IF NOT EXISTS address (
	id 				SERIAL PRIMARY KEY,
	city 			VARCHAR(255) NOT NULL,
	street			VARCHAR(255) NOT NULL,
	city_code 		INT NOT NULL,
	house_number 	INT NOT NULL
);

CREATE TABLE IF NOT EXISTS customer (
	id 				SERIAL PRIMARY KEY,
	firstname		VARCHAR(255) NOT NULL,
	lastname		VARCHAR(255) NOT NULL,
	age				INT NOT NULL,
	address_id		INT,
	CONSTRAINT fk_customer_address
		FOREIGN KEY (address_id) REFERENCES address(id)
);

CREATE TABLE IF NOT EXISTS processing_status (
	id				SERIAL PRIMARY KEY,
	status_name		VARCHAR(255) NOT NULL,
	responsible		VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS "order" (
	id				SERIAL PRIMARY KEY,
	customer_id		INT NOT NULL,
	order_date		TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	status_id		INT NOT NULL,
	CONSTRAINT fk_order_customer
		FOREIGN KEY (customer_id) REFERENCES customer(id),
	CONSTRAINT fk_order_status
		FOREIGN KEY (status_id) REFERENCES processing_status(id)
);

CREATE TABLE IF NOT EXISTS product (
	id				SERIAL PRIMARY KEY,
	name			VARCHAR(255) NOT NULL,
	category		VARCHAR(255),
	single_price	FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS transaction (
	order_id		INT NOT NULL,
	product_id		INT NOT NULL,
	amount			INT NOT NULL,

	PRIMARY KEY (order_id, product_id),

	CONSTRAINT fk_transaction_oder
		FOREIGN KEY (order_id) REFERENCES "order"(id),
	CONSTRAINT fk_transaction_product
		FOREIGN KEY (product_id) REFERENCES product(id)
);


SELECT sum(p.single_price * t.amount) AS total_revenue
FROM transaction t
JOIN product p ON t.product_id = p.id;

SELECT c.id AS customer_id, c.firstname, c.lastname, SUM(p.single_price * t.amount) AS total_spent
FROM customer c
JOIN "order" o ON c.id = o.customer_id
JOIN transaction t ON o.id = t.order_id
JOIN product p ON t.product_id = p.id
GROUP BY c.id, c.firstname, c.lastname
ORDER BY total_spent DESC;

SELECT ps.status_name, COUNT(o.id) AS order_count
FROM processing_status ps
LEFT JOIN "order" o ON ps.id = o.status_id
GROUP BY ps.status_name;    
