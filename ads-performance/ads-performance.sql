/* Write your PL/SQL query statement below */
select ad_id, case sum(total) when 0 then 0.00 else round(sum(clicked)*100/sum(total),2) end as ctr from(select ad_id,action,case when action = 'Viewed' or action = 'Clicked' then count(action) else 0 end as total, case when action = 'Clicked' then count(action) else 0 end as clicked
from Ads
group by ad_id,action)
group by ad_id
order by ctr desc, ad_id


