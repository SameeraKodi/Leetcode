/* Write your PL/SQL query statement below */


with test as
(select match_id,host_team,guest_team,
case when host_goals > guest_goals then 3 
when host_goals = guest_goals then 1
else 0 end as host_points,
case when guest_goals > host_goals then 3
when guest_goals = host_goals then 1
else 0 end as guest_points
from matches)
,
test_2 as
(select * 
from(select host_team as id, host_points as scores
from test)
union all
(select guest_team as id,guest_points as scores
from test))




select B.team_id, B.team_name, NVL(SUM(A.scores),0) as num_points 
from test_2 A right outer join Teams B on A.id=B.team_id
    group by B.team_id, B.team_name
    order by 3 DESC, 1