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