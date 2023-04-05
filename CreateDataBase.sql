-- create new table in new database

CREATE DATABASE IF NOT EXISTS sql_store2;
USE sql_store2;
CREATE TABLE customers
(
	customer_id INT PRIMARY KEY auto_increment,
    first_name varchar(50) NOT NULL,
    points 		INT NOT NULL default 0,
    email		VARCHAR(255) NOT NULL UNIQUE
);

-- DELETE new table in new database

CREATE DATABASE IF NOT EXISTS sql_store2;
USE sql_store2;
DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers
(
	customer_id INT PRIMARY KEY auto_increment,
    first_name varchar(50) NOT NULL,
    points 		INT NOT NULL default 0,
    email		VARCHAR(255) NOT NULL UNIQUE
);

-- ALTERING TABLES

ALTER TABLE customers
add last_name varchar(50) NOT NULL AFTER first_name,
    add city 	varchar(50) not null
MODIFY COLUMN first_name VARCHAR(55) DEFAULT '',#=edit column
    DROP points #=delete column
;

-- Create primary key and foreign key 

CREATE DATABASE IF NOT EXISTS sql_store2;
USE sql_store2;
DROP TABLE IF EXISTS customers;
CREATE TABLE IF NOT EXISTS customers
(
customer_id INT PRIMARY KEY auto_increment,
    first_name varchar(50) NOT NULL,
    points 		INT NOT NULL default 0,
    email		VARCHAR(255) NOT NULL UNIQUE
);
DROP TABLE IF EXISTS orders;
CREATE TABLE orders
(
	order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    FOREIGN KEY fk_orders_customers (customer_id)
		REFERENCES customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

-- ALTER PRIMARY AND FOREIGN KEY

ALTER TABLE customers
	add last_name varchar(50) NOT NULL AFTER first_name,
    add city 	varchar(50) not null,
	MODIFY COLUMN first_name VARCHAR(55) DEFAULT '',
    DROP points
    ;
    
ALTER TABLE orders
	ADD PRIMARY KEY (order_id),
    DROP PRIMARY KEY,
    DROP FOREIGN KEY fk_orders_customers,
    ADD FOREIGN KEY fk_orders_customers (customer_id)
		REFERENCES customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION;


