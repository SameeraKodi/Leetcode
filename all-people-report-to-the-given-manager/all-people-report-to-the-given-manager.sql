/* Write your PL/SQL query statement below */
select employee_id
from employees
where employee_id !=1 and( manager_id = 1 or manager_id in (select employee_id from employees where manager_id = 1 or manager_id in (select employee_id from employees where manager_id = 1 or manager_id in (select employee_id from employees where manager_id = 1  ))) );