/* Write your PL/SQL query statement below */

select name 
from salesperson
where name NOT IN
(select s.name
from orders o join company c on o.com_id = c.com_id join salesperson s on s.sales_id = o.sales_id
where c.name = 'RED')
