/* Write your PL/SQL query statement below */
select customer_number as "customer_number"
from orders
having count(order_number) = (select max(count(order_number)) from orders group by customer_number)
group by customer_number
​
