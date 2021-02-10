/* Write your PL/SQL query statement below */
select customer_id,name 
from(select c.customer_id,name,sum(quantity*price) as spent
from orders o join product p on o.product_id = p.product_id 
join customers c on c.customer_id = o.customer_id
where to_char(order_date,'MON') = 'JUN'
--having sum(quantity*price) >= 100
group by c.customer_id,name)
where spent >=100
INTERSECT
select customer_id,name 
from(select c.customer_id,name,sum(quantity*price) as spent
from orders o join product p on o.product_id = p.product_id 
join customers c on c.customer_id = o.customer_id
where to_char(order_date,'MON') = 'JUL'
--having sum(quantity*price) >= 100
group by c.customer_id,name)
where spent >=100


