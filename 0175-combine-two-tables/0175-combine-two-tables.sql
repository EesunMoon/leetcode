# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p Left join Address a on p.personID = a.personID;