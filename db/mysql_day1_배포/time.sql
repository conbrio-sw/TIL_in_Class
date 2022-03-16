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