/* Write your PL/SQL query statement below */

with sam as (select product_id as binary , max(change_date) as test
            from Products
            where change_date <= '2019-08-16'
            group by product_id),
            

lam as(select *
from Products p left join sam s on p.product_id = s.binary)



select distinct product_id,case when test is null then 10 else new_price end as "price" 
from lam 
where test is null or change_date = test



 