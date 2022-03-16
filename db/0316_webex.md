- like 사용

  ```mysql
  -- m으로 시작하는 모든것 -- 
  SELECT * FROM sakila.customer
  where first_name like binary '%M';
  -- %는 어떤 문자가 무제한 길이, _는 한글자 아무거나 --
  
  SELECT * FROM sakila.customer
  where first_name like binary '%M%E%';
  
  -- !! 주의 --
  INDEX 컬럼 first_name =======> LIKE "LO%" <===== 만들어진 INDEX를 이용(탄다)
  INDEX 컬럼 first_name =======> LIKE "%LO%" <===== 만들어진 INDEX를 이용 X
  
  ```

  

- order by 사용

  ```mysql
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
  ```

- limit

  ```mysql
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
  ```

- 문자열 조작

  ```mysql
  
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
  select char_length('한글'), length('한글'), char_length('eng'), length('eng') ;
  -- INSTR, 1부터 시작, 없으면 0 리턴
  -- 0보다 크면 cde가 앞 문자열 안에 있다는 뜻 (where조건에서 씀)
  select instr('ABCDEFG', 'CDE');
  select * from sakila.country
  where instr(country, 'AU') > 0;
  -- index 필요할 경우, INSTR
  -- 포함관계 ==> LIKE 쓰는 게 맞다 (function 사용하면 느리다)
  ```

- 날짜 시간

  ```mysql
  -- TIMEZONE
  -- UTC 세계 표준 시
  
  -- 우리는 한국 시간이 기준이다
  select @@time_zone;
  select curdate();
  select now(); -- Asia / seoul
  
  select utc_date();
  select utc_time();
  
  -- 이렇게 하면 수정시간 넣을 수 있다.
  insert ..now();
  
  -- 날자데이터 추출, 다만 프론트부분에서 하는것이 낫다
  -- 가장 간단한 %Y%m%d 형태로 보내는 것이 좋다
  -- DATE => String
  select last_update, date_format(last_update, '%Y%m%d') from sakila.country;
  -- str_to-date
  -- / 같은 것이 있으면 /로 잘라줘야한다.
  select str_to_date('2022/0316', '%Y/%m%d');
  -- DATEDIFF-- 날짜 차이 계산
  -- 형태가 조금 달라도 생각해준다
  select datediff('2022-05-27', '20220316');
  select last_update, datediff('2006-03-15', last_update) from sakila.country;
  -- date_add
  select date_add('2022-03-16', interval 2 Month);
  select date_add(now(), interval 20 day);
  -- WEEKDAY
  -- 월화수목금 알려준다
  select weekday('2022-05-27'); -- Zero base 0:월 ... 6:일
  ```

- round, ceil, 

  ```mysql
  -- 반올림
  select round(123.456, 1);
  select round(123.456, -1);
  -- 올림
  select ceil(123.456);
  -- 내림
  select floor(123.456);
  ```

- ifnull & case when then

  ```mysql
  -- ifnull
  -- null 인 경우만 바꿔주기, 오라클에서는 nvn
  select address, address2,ifnull(address2, 'A') from sakila.address;
  -- case when then else end
  -- if else 처럼 쓸 수 있는 애
  select first_name, last_name, 
  	case when store_id = 1 then 'ONE'
  		 when store_id = 2 then 'TWO'
  		 else 'ETC'
      end as STORE_BLOCK
   from sakila.customer;
  ```

- Insert

  - ```mysql
    INSERT INTO `test`.`customer` (`customer_id`, `customer_nm`) VALUES ('1', '홍길동');
    INSERT INTO `test`.`product` (`product_id`, `product_nm`, `product_price`) VALUES ('111', 'TV', '1000');
    INSERT INTO `test`.`product` (`product_id`, `product_nm`, `product_price`) VALUES ('222', '냉장고', '2000');
    INSERT INTO `test`.`customer_order` 
                (`order_id`, `customer_id`, `product_id`, `order_price`) 
         VALUES ('11', '1', '111', '1000');
    ```

- Delete

  - ```mysql
    -- foregin key로 연결된 테이블에서 사용 중이면 삭제가 안된다.
    DELETE FROM customer
    where customer_id = 1;
    ```

- Group By

  - ```mysql
    -- row 1개 1개 대신 row를 합치는 방식
    use ssafydb;
    select count(*) from employees;
    
    -- 그룹 바이를 기준으로 펼치게 된다.
    select department_ID, count(*) from employees
    where department_id > 50
    group by department_id;
    select job_id, count(*) from employees
    where department_id > 50
    group by job_id;
    
    -- sum
    select department_ID, sum(salary) from employees
    group by department_id
    order by sum(salary) desc;
    
    -- min,max, avg
    select Min(salary), max(salary), avg(salary) from employees;
    -- 그룹 바이가 중첩이 가능하다
    select department_ID, job_id, (salary), max(salary), avg(salary) from employees
    group by department_id, job_id;
    
    -- having 그룹 바이를 했을 때 그 결과로 조건 사용 가능
    select department_id, avg(salary) from employees
    group by department_id
    having avg(salary) > 5000;
    
    -- window function
    -- over partition by
    select employee_id, department_id,avg(salary) over (partition by department_id)
    from employees;
    ```

  - 

- Primary Key

  - 테이블에서 row에 대한 식별자
  - 중복 불가
  - Not Null, Naturally

- Unique Key

  - 테이블에서 row에 대한 식별자
  - 중복 불가
  - Can Be Null
  - 여러 개의 Unique Key Column을 가질 수 있음
  - database 마다 정책이 다름
  - MySQL은 Null을 허용하고, 복수 개의 Null도 허용

- Foreign Key 매우 중요

  - 분리된 테이블의 관계를 형성
  - 데이터의 무결성을 위한 제약 조건
  - 테이블에 부여되는 별도의 객체
  - FK로 관계된 테이블의 Key 값의 집합을 유지해야 함
  - 기존 테이블(게시판) 등록 / 수정 <- 참조된 테이블 (회원) check
  - 참조된 테이블(회원) 삭제 <- 기존 테이블(게시판) check
  - `Alter table`에서 바꿔주기

- 대용량 Data

  - 검색 속도 개선
  - 대략 분포도가 30% 미만일 경우 효과를 볼 수 있다.
  - index 컬럼이 많아지면 그 만큼 insert / delete / update에서 손해를 본다
    - like 검색할 때  % 가 맨 앞에 있으면 full로 찾는다
    - not in도 full로 찾는다 (%와 상관없이)
  - 올바른 SQL을 작성하지 않으면 index를 타지 않는 경우 발생
    - function
      - 왼쪽은 그대로 둬야한다.
      - upper 같은 함수를  index를 타지 못한다.
    - NOT IN

### PL-SQL

- DBMS Dependent
- 함수, 프로시저 등으로 이루어짐
  - 함수는 상대적으로 간단
  - 프로시저는 복잡
- 

