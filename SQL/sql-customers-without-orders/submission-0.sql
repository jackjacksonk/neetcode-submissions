-- Write your query below
-- SELECT customers_id, name
-- FROM customers, orders
-- WHERE customer_id < 1

SELECT name
FROM customers
WHERE id NOT IN (SELECT customer_id FROM orders)