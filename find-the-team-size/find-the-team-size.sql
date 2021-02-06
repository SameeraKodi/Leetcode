/* Write your PL/SQL query statement below */
select employee_id,count(team_id) over(partition by team_id) as "team_size"
from Employee
group by employee_id,team_id
order by employee_id
