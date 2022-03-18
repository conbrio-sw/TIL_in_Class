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
where co.name like 'United%';

-- 6
SELECT 
    COUNT(DISTINCT cl.CountryCode) AS '국가수'
FROM
    countrylanguage cl
WHERE
    cl.IsOfficial = 'T'
        AND cl.Percentage > (SELECT 
            MAX(cl.Percentage)
        FROM
            countrylanguage cl
        WHERE
            cl.CountryCode = 'che'
                AND cl.IsOfficial = 'T');


-- 7
SELECT 
    cl.language
FROM
    countrylanguage cl
WHERE
    cl.CountryCode = (SELECT 
            Code
        FROM
            country
        WHERE
            Name = 'south korea')
        AND cl.IsOfficial = 'T';


SELECT cl.language
FROM   countrylanguage cl,
       (SELECT code
        FROM   country
        WHERE  NAME = 'south korea') sk
WHERE  cl.countrycode = sk.code
       AND cl.isofficial = 'T'; 

SELECT cl.language
FROM   countrylanguage cl,
       country co
WHERE  co.NAME = 'south korea'
       AND cl.countrycode = co.code
       AND cl.isofficial = 'T'; 


-- 8

SELECT NAME,
       code,
       (SELECT Count(id)
        FROM   city
        WHERE  city.countrycode = code) '도시 개수'
FROM   country
WHERE  NAME LIKE 'bo%'
       AND population != 0; 


SELECT c.NAME,
       c.code,
       t.cnt
FROM   country c,
       (SELECT countrycode,
               Count(countrycode) cnt
        FROM   city
        GROUP  BY countrycode) t
WHERE  c.NAME LIKE 'bo%'
       AND c.code = t.countrycode; 

SELECT c.NAME,
       c.code,
       Count(ci.ID) cnt
FROM   country c,
       city ci
WHERE  c.code = ci.countrycode
       AND c.NAME LIKE 'bo%'
GROUP  BY c.code; 



-- 9
SELECT NAME,
       code,
       CASE
         WHEN (SELECT Count(id)
               FROM   city
               WHERE  city.countrycode = code) = 0 THEN '단독'
         ELSE (SELECT Count(id)
               FROM   city
               WHERE  city.countrycode = code)
       END'도시 개수'
FROM   country
WHERE  NAME LIKE 'bo%';

SELECT c.NAME,
       c.code,
       Ifnull(t.cnt, '단독') '도시개수'
FROM   country c
       LEFT JOIN (SELECT countrycode,
                         Count(countrycode) cnt
                  FROM   city
                  GROUP  BY countrycode) t
              ON c.code = t.countrycode
WHERE  c.NAME LIKE 'bo%';

SELECT c.NAME,
       c.code,
       CASE
         WHEN Count(ci.id) = 0 THEN '단독'
         ELSE Count(ci.id)
       END '도시 개수'
FROM   country c
       LEFT JOIN city ci
              ON c.code = ci.countrycode
WHERE  c.NAME LIKE 'bo%'
GROUP  BY c.code; 

-- 10
SELECT countrycode,
       NAME,
       population
FROM   city
WHERE  population = (SELECT Max(population)
                     FROM   city); 

-- 11
SELECT (SELECT NAME
        FROM   country
        WHERE  code = countrycode) 'name',
       countrycode,
       NAME,
       population
FROM   city
WHERE  population = (SELECT Min(population)
                     FROM   city); 


select co.name, co.code, t.name, t.Population
  from country co,
       ( select countryCode, name, population
          from city
         where population = (select min(population) from city) ) t
 where co.Code = t.countryCode;


-- 12
SELECT c.countrycode,
       c.NAME,
       c.population
FROM   (SELECT *
        FROM   city
        WHERE  population > (SELECT population
                             FROM   city
                             WHERE  NAME = 'seoul')) c; 

SELECT countrycode,
       NAME,
       population
FROM   city
WHERE  population > (SELECT population
                     FROM   city
                     WHERE  countrycode = 'KOR'
                            AND NAME = 'seoul'); -- 서울 인구


SELECT ci1.countrycode,
       ci1.NAME,
       ci1.population
FROM   city ci1,
       city ci2
WHERE  ci2.countrycode = 'KOR'
       AND ci2.NAME = 'seoul'
       AND ci1.population > ci2.population; 

-- 13
SELECT sm.countrycode,
       cl.language
FROM   (SELECT *
        FROM   city
        WHERE  NAME = 'san miguel') sm,
       countrylanguage cl
WHERE  sm.countrycode = cl.countrycode
       AND cl.isofficial = 'T'; 



SELECT countrycode,
       language
FROM   countrylanguage
WHERE  isofficial = 't'
       AND countrycode IN (SELECT countrycode
                           FROM   city
                           WHERE  NAME = 'san miguel');
                           
SELECT cl.countrycode,
       cl.language
FROM   countrylanguage cl,
       city ci
WHERE  cl.isofficial = 't'
       AND ci.NAME = 'san miguel'
       AND cl.countrycode = ci.countrycode;

-- 14
SELECT countrycode,
       Max(population) 'max_pop'
FROM   city
GROUP  BY countrycode
ORDER  BY countrycode; 

-- 15
SELECT t.countrycode,
       t.NAME,
       t.max_pop
FROM   (SELECT *, Max(population) 'max_pop'
        FROM   city
        GROUP  BY countrycode
        ORDER  BY countrycode) t;

select countrycode, NAME, population
from city
where(countrycode, population) in (SELECT countrycode,
       Max(population)
FROM   city
GROUP  BY countrycode)
order by countrycode;

-- 16
SELECT t.countrycode,
       c.NAME,
       t.NAME,
       t.population
FROM   country c
       LEFT JOIN(SELECT *
                 FROM   city
                 GROUP  BY countrycode
                 ORDER  BY countrycode) t
              ON c.code = t.countrycode; 


SELECT t.countrycode,
       co.NAME,
       co.code,
       t.population
FROM   country co
       LEFT OUTER JOIN (SELECT countrycode, NAME, population
        FROM   city
        WHERE ( countrycode, population ) IN (SELECT countrycode, Max(population)
                                              FROM   city
                                              GROUP  BY countrycode)) t
                    ON co.code = t.countrycode; 


-- 17

create or replace view summary as
SELECT t.countrycode,
       co.NAME co_name,
       t.name ci_name,
       t.population
FROM   country co
       LEFT OUTER JOIN (SELECT countrycode, NAME, population
        FROM   city
        WHERE ( countrycode, population ) IN (SELECT countrycode, Max(population)
                                              FROM   city
                                              GROUP  BY countrycode)) t
                    ON co.code = t.countrycode; 


select *
from city;
select *
from country;
select *
from countrylanguage;