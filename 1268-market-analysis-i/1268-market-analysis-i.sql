# Write your MySQL query statement below

SELECT u.user_id as buyer_id, u.join_date, count(o.order_id) as orders_in_2019
FROM Users u left join Orders o on u.user_id = o.buyer_id and year(o.order_date) = "2019"
Group by u.user_id;
