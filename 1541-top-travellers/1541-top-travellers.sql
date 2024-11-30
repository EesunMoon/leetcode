# Write your MySQL query statement below

SELECT u.name, IFNULL(sum(r.distance), 0) as travelled_distance
FROM Users u left join rides r on u.id = r.user_id
Group by u.id
Order by travelled_distance desc, u.name asc;