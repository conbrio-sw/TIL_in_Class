-- 1
use world;

-- 2
desc city;
desc country;
desc countrylanguage;

-- 3
select * from world.country
where Code = 'KOR';

-- 4
select code, name, gnp, GNPOld, gnp-GNPOld as gnp변동량 from world.country
where gnp-GNPOld > 0
order by gnp-GNPOld;

-- 5
select distinct Continent from world.country
order by length(continent);

-- 6
select concat(name, '은 ', region, '에 속하며 인구는 ', population, '명이다.') as 정보 from country
where continent = 'asia'
order by name;

-- 7
select name, continent, gnp, population from country
where IndepYear is null
and Population >= 10000
order by Population;

-- 8
select code, name, Population from country
where Population between 100000000 and 200000000
order by Population desc
limit 3;

-- 9
select code, name, IndepYear from country
where IndepYear in (800, 1810, 1811, 1901)
order by IndepYear, code desc;

-- 10
select code, name, region from country
where Region like '%asia%'
and name like '_o%';

-- 11
select char_length('홍길동') as 한글, char_length('hong') as 영문;

-- 12
select code, name, GovernmentForm from country
where GovernmentForm like '%republic%'
and char_length(name) >= 10
order by char_length(name) desc
limit 10;

-- 13 left 대신에 substr(code, 1, 1)로 사용가능
select code, name from country
where left(code, 1) in ('a', 'e', 'i', 'o', 'u')
order by name
limit 2, 3; 

-- 14
select name, concat(left(name,2), lpad('*', char_length(name)-4,'*') ,right(name,2)) as guess from country;

-- 15
select distinct replace(region, ' ', '_') as 지역들 from country
order by char_length(region) desc;

-- 16
select name, SurfaceArea, population, round(SurfaceArea/population, 3) as '1인당 점유면적'  from country
where Population >= 100000000
order by SurfaceArea/population;

-- 17
select curdate() as '오늘', datediff(curdate(), '2022-01-01') as '올해 지난 날', date_add(curdate(), interval 100 day) as '100일 후';

-- 18
select name, Continent, LifeExpectancy,
case when LifeExpectancy > 80 then '장수국가'
	 when LifeExpectancy > 60 then '일반국가'
     else '단명국가'
     end as '구분'
     from country
 where Continent = 'Asia'
 and LifeExpectancy is not null
order by LifeExpectancy;

-- 19
select name, gnp, gnpold, ifnull(gnp-GNPOld, '신규') as 'gnp 향상' from country
order by name;

-- 20
select weekday('2022-05-05'),
case when weekday('2022-05-05') in (5, 6) then '불행'
else '행복'
end as '행복여부';

select weekday('2022-05-05'), if(weekday('2022-05-05')>4, '불행', '행복') as '행복 여부';