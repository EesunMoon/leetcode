# Write your MySQL query statement below
SELECT customer_id, Count(*) AS count_no_trans
FROM Visits v left join Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id is null
Group by customer_id;