use test;
select co.order_id, co.customer_id, co.product_id,
co.order_price, c.customer_nm, p.product_price
from customer_order co, customer c, product p
where co.product_id = p.product_id
and co.customer_id = c.customer_id;

-- 고객의 주문 정보를 처리
-- 원장 테이블 마스터 테이블 / 거래 테이블 이력 테이블
-- 사원 : 직책 컬럼
-- A 고객 1000원 구매 2012-3-15,  이후에 product.price => 2000 2022-3-16
select co.order_id, co.customer_id, co.product_id, 
co.order_price, c.customer_nm
from customer_order co, customer c
where co.customer_id = c.customer_id;

select co.order_id, co.customer_id, co.product_id, 
co.order_price, c.customer_nm
from customer c left outer join customer_order co
on co.customer_id = c.customer_id