-- database: :memory:
-- <!-- Parallel Database Architecture for Large E-commerce Website (Using Neon PostgreSQL)
-- 1. Architecture Design
-- Frontend layer: Handles user requests from web or mobile clients.
-- Application layer: Contains business logic and API endpoints.
-- Parallel database layer (Neon PostgreSQL):
-- Coordinator node: Receives queries through a Neon PostgreSQL endpoint, plans execution, and aggregates results.
-- Multiple data nodes: Neon automatically shards and replicates data across distributed storage and compute nodes.
-- Network: Provides high-speed interconnect between Neon compute and storage layers.
-- Note: Neon PostgreSQL is a serverless, distributed PostgreSQL solution that separates storage and compute, enabling parallel query execution and elastic scaling. 

--2. Database Schema and Sample Queries

-- Create a new database (run as a superuser or via Neon dashboard)
--CREATE DATABASE ecommerce_db;

SELECT current_database();
-- Connect to the new database

--\c ecommerce_db 

-- Create tables for a large e-commerce website
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL,
    stock INT NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    order_date TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

-- Insert sample data (repeat or use a script for large volumes)
INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com'), ('bob', 'bob@example.com');
INSERT INTO products (name, description, price, stock) VALUES
('Laptop', 'Gaming Laptop', 1200.00, 50),
('Phone', 'Smartphone', 800.00, 100);

INSERT INTO orders (user_id) VALUES (1), (2);
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 1200.00),
(2, 2, 2, 1600.00);

-- Example query: Get total sales per product
EXPLAIN ANALYZE
SELECT p.name, SUM(oi.quantity * oi.price) AS total_sales
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.name
ORDER BY total_sales DESC;

-- Example query: Get top users by order count
EXPLAIN ANALYZE
SELECT u.username, COUNT(o.order_id) AS order_count
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.username
ORDER BY order_count DESC;

-- To measure performance, use EXPLAIN ANALYZE before your queries.
-- For large-scale testing, use tools like pgbench or generate large datasets.
