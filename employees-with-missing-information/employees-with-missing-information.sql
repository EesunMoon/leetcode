# Write your MySQL query statement below
SELECT employee_id
FROM employees
Where employee_id not in (select employee_id from salaries)
UNION
Select employee_id
From salaries
where employee_id not in (select employee_id from employees)
Order by employee_id asc;