/* Write your PL/SQL query statement below */
​
select player_id as "player_id",to_char(min(event_date),'YYYY-MM-DD')as "first_login"
from Activity
group by player_id;
​
​
