-- Revising the select Query I
select *
from city
where countrycode = 'USA'
and population > 100000;

-- Revising the select Query II
select name
from city
where countrycode = 'USA'
and population > 120000;

-- Weather observation station III
select DISTINCT city
from station
where mod(id,2) = 0