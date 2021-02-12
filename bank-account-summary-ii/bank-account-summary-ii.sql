/* Write your PL/SQL query statement below */



select name,sum(amount) as balance
from users u left join transactions t on u.account = t.account
having sum(amount) > 10000
group by name
