create database dbtest
default character set utf8mb3 collate utf8mb3_general_ci;

use dbtest;
create table test (
val varchar(10)
);

insert into test(val)
values('a');

insert into test(val)
values('👍');


select *
from test;

drop database dbtest;












create database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;

use dbtest;
create table test (
val varchar(10)
);

insert into test(val)
values('a');

insert into test(val)
values('👍');


select *
from test;







alter database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;

drop database dbtest;

use ssafydb;

-- 회원 정보 table 생성.
-- table name : ssafy_member
-- column
-- idx			int			auto_increments		PK
-- userid		varchar(16)	not null
-- username		varchar(20)
-- userpwd		varchar(16)
-- emailid		varchar(20)
-- emaildomain	varchar(50)
-- joindate		timestamp	default	current_timestamp

create table ssafy_member (
	idx			int			auto_increment,
    userid		varchar(16)	not null,
username		varchar(20),
userpwd		varchar(16),
emailid		varchar(20),
emaildomain	varchar(50),
joindate		timestamp	default	current_timestamp,
primary key (idx)

);
select *
from ssafy_member;




-- 회원 정보 등록
-- 'kimssafy', '김싸피', '1234', 'kimssafy', 'ssafy.com' 등록시간

insert into ssafy_member (userid, username, userpwd, emailid, emaildomain, joindate)
values('kimssafy', '김싸피', '1234', 'kimssafy', 'ssafy.com', now());

select *
from ssafy_member;

-- '김싸피', 'kimssafy', '1234'
insert into ssafy_member(username, userid, userpwd)
values('이싸피', 'leessafy', '1234'),
('박싸피', 'parkssafy', '9876');

select *
from ssafy_member;

-- '이싸피', 'leessafy', '1234'
-- '박싸피', 'parkssafy', '9876'



-- userid가 kimssafy인 회원의 비번을 9876, 이메일 도메인을 ssafy.co.kr으로 변경.

update ssafy_member
set userpwd = '9876', emaildomain = 'ssafy.co.kr'
where userid='kimssafy';

commit;

-- userid가 kimssafy 회원 탈퇴


delete from ssafy_member
where userid='kimssafy';

rollback;

