# Write your MySQL query statement below

SELECT customer_number
FROM Orders
Group by customer_number
ORDER BY Count(*) DESC
limit 1;