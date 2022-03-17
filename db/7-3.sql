use world;
select *
from city;
select *
from country;
select *
from countrylanguage;

-- 1
select country.code, country.name
from city, country
where city.Name = 'Kabul'
and city.CountryCode = country.Code;

-- 2
select co.name, cl.Language, cl.Percentage
from country co, countrylanguage cl
where cl.Percentage = '100.0'
and co.code = cl.CountryCode
and cl.IsOfficial = 'T'
order by co.name;

-- 3
select ci.name, cl.Language, co.name
from city ci, country co, countrylanguage cl
where ci.name = 'amsterdam'
and ci.CountryCode = co.code
and cl.CountryCode = co.code
and cl.IsOfficial = 'T';

-- 4
select co.name, co.capital, ci.name '수도', ci.Population '수도 인구' 
from city ci, country co
where co.name like 'United%'
and co.capital = ci.ID;

-- 5
select co.name, co.capital, ifnull(ci.name, '수도 없음') '수도', ifnull(ci.Population, '수도 없음') '수도 인구' 
from country co left outer join city ci
on co.capital = ci.ID
where co.name like 'United%'

