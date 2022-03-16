
-- 맨 앞 10개 --
SELECT * FROM sakila.city
limit 10;

-- offset , 15개 건너 띄기 --
-- 페이징 기본
SELECT * FROM sakila.city
limit 10 offset 15;

-- 하나로 줄이기, 순서가 바뀜
SELECT * FROM sakila.city
limit 15, 10;