-- 오름차순이 디폴트 --

-- 내림차순 --
SELECT * FROM sakila.customer
order by first_name DESC;

-- FETCH 대상 확정하는 것이 where 절--
-- order by로 이후 정렬 --
SELECT * FROM sakila.customer
where store_id = 1
order by store_id DESC, first_name asc;

-- 2개 이상으로 정렬할 때 , 로 구분 --
select * from sakila.city
where country_id in (86, 103)
order by country_id desc, city