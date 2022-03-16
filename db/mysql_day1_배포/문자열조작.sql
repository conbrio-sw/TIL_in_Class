
-- concat으로 문자열 합치기
SELECT concat(first_name, '-', last_name) as full_name FROM sakila.customer;

-- replace로 문자열 중 문자 바꾸기
-- replace는 replaceAll 개념
select email, replace(email, '.', '_') from customer;

select * from sakila.category;
-- LPAD, 부족한 문자열 채우기 왼쪽부터.
select lpad(NAME, 20, ' ') from sakila.category;
-- LPAD로 복사 개념으로 쓸 수 있다.
select lpad('*', 5, '*');
-- 왼쪽에서부터 3개 잘라서 들고옴
select name, left(name, 3), right(name,2) from sakila.category;
-- LENGTH(BYTE), CHAR_LENGTH(글자단위) 구별해야한다
-- 한글은 한글자 당 3BYTE, 영문은 1BYTE
select name, length(name), char_length(name) from sakila.category;
select char_length('한글'), length('한글'), char_length('eng'), length('eng');
-- INSTR, 1부터 시작, 없으면 0 리턴
-- 0보다 크면 cde가 앞 문자열 안에 있다는 뜻 (where조건에서 씀)
select instr('ABCDEFG', 'CDE');
select * from sakila.country
where instr(country, 'AU') > 0;
-- index 필요할 경우, INSTR
-- 포함관계 ==> LIKE 쓰는 게 맞다 (function 사용하면 느리다)