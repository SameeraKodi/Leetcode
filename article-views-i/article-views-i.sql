/* Write your PL/SQL query statement below */
select distinct viewer_id as "id"
from Views
where author_id = viewer_id
order by viewer_id
​