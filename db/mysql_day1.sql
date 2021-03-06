create database dbtest
default character set utf8mb3 collate utf8mb3_general_ci;

use dbtest;
create table test (
val varchar(10)
);

insert into test(val)
values('a');

insert into test(val)
values('๐');


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
values('๐');


select *
from test;







alter database dbtest
default character set utf8mb4 collate utf8mb4_general_ci;

drop database dbtest;

use ssafydb;

-- ํ์ ์ ๋ณด table ์์ฑ.
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




-- ํ์ ์ ๋ณด ๋ฑ๋ก
-- 'kimssafy', '๊น์ธํผ', '1234', 'kimssafy', 'ssafy.com' ๋ฑ๋ก์๊ฐ

insert into ssafy_member (userid, username, userpwd, emailid, emaildomain, joindate)
values('kimssafy', '๊น์ธํผ', '1234', 'kimssafy', 'ssafy.com', now());

select *
from ssafy_member;

-- '๊น์ธํผ', 'kimssafy', '1234'
insert into ssafy_member(username, userid, userpwd)
values('์ด์ธํผ', 'leessafy', '1234'),
('๋ฐ์ธํผ', 'parkssafy', '9876');

select *
from ssafy_member;

-- '์ด์ธํผ', 'leessafy', '1234'
-- '๋ฐ์ธํผ', 'parkssafy', '9876'



-- userid๊ฐ kimssafy์ธ ํ์์ ๋น๋ฒ์ 9876, ์ด๋ฉ์ผ ๋๋ฉ์ธ์ ssafy.co.kr์ผ๋ก ๋ณ๊ฒฝ.

update ssafy_member
set userpwd = '9876', emaildomain = 'ssafy.co.kr'
where userid='kimssafy';

commit;

-- userid๊ฐ kimssafy ํ์ ํํด


delete from ssafy_member
where userid='kimssafy';

rollback;

