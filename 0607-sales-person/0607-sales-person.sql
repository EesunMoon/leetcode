# Write your MySQL query statement below

SELECT distinct name
FROM SalesPerson
WHERE sales_id not in (SELECT o.sales_id
FROM Company c, Orders o
WHERE c.com_id = o.com_id and c.name = "RED");


