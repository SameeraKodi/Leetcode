/* Write your PL/SQL query statement below */

select extra as "report_reason",count(post_id) as "report_count"
from(select distinct post_id, extra
from Actions
where action_date = '2019-07-04' and extra is not null and action = 'report')
group by extra





