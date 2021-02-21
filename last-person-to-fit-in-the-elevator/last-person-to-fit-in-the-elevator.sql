/* Write your PL/SQL query statement below */
with test as
(select person_id,person_name,turn,sum(weight) over(order by turn)  total
from queue)



select person_name
from test
where total <= 1000 and turn = (select max(turn) from test where total <= 1000)





