/* Write your PL/SQL query statement below */

select round(count(t2.player_id)/count(distinct t1.player_id),2) as fraction from (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id)t1 LEFT JOIN Activity t2
ON t1.player_id = t2.player_id AND t1.first_login = t2.event_date - 1;

