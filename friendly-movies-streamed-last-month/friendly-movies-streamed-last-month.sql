/* Write your PL/SQL query statement below */
select distinct title
from tvprogram t join content c on t.content_id = c.content_id and to_char(t.program_date,'MM') = '06'
where kids_content = 'Y' and content_type = 'Movies'