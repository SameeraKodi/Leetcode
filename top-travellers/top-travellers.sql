/* Write your PL/SQL query statement below */
select name as "name", nvl(dist,0) as "travelled_distance"
from(select u.id, name,sum(distance) as dist
from users u left join rides r on r.user_id = u.id
group by u.id,name)
order by nvl(dist,0) desc,name asc;

