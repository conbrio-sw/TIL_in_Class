-- m으로 시작하는 모든것 -- 
SELECT * FROM sakila.customer
where first_name like binary '%M';
-- %는 어떤 문자가 무제한 길이, _는 한글자 아무거나 --




SELECT * FROM sakila.customer
where first_name like binary '%M%E%';

-- !! 주의 --
INDEX 컬럼 first_name =======> LIKE "LO%" <===== 만들어진 INDEX를 이용(탄다)
INDEX 컬럼 first_name =======> LIKE "%LO%" <===== 만들어진 INDEX를 이용 X
