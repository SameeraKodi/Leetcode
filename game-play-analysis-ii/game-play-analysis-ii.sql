/* Write your PL/SQL query statement below */
select player_id as "player_id",device_id as "device_id"
from Activity
where (player_id,event_date) IN (select player_id,min(event_date) from Activity group by player_id)
order by player_id
