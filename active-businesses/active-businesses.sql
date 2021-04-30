/* Write your PL/SQL query statement below */

select business_id
from(select business_id,event_type, case when occurences > avg_occ then 1 else 0 end as c
from(select business_id,event_type,occurences,avg(occurences) over(partition by event_type) as avg_occ from Events))
group by business_id
having sum(c) > 1



