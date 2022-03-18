SELECT co.order_id, co.customer_id, c.customer_nm, 
       co.product_id, p.product_nm, co.order_price, p.product_price
  FROM customer_order co, customer c, product p
 WHERE co.customer_id = c.customer_id
   AND co.product_id = p.product_id
   AND p.product_price <= 1500;
   
   
   
-- SELECT co.order_id, co.customer_id, c.customer_nm, co.product_id, co.order_price
-- 		,( select p.product_nm
-- 			from product p
--             where p.product_price < 5000) product_nm,
-- 		( select p.product_price
-- 			from product p
--             where co.product_id = p.product_id
--             and  p.product_price > 1500) product_price
--   FROM customer_order co, customer c
--  WHERE co.customer_id = c.customer_id;


SELECT co.order_id, co.customer_id, c.customer_nm, 
       co.product_id, p.product_nm, co.order_price, p.product_price
  FROM customer_order co, customer c, 
	   (select product_nm, product_price, product_id 
       from product
       where product_price <= 1500) p
 WHERE co.customer_id = c.customer_id
   AND co.product_id = p.product_id;
   

-- from 절에 p가 없기 때문에 p_pirce, id를 가져올 방법이 없다.
-- = 쓰면 반드시 1개만 나와야한다.  2개 이상 볼려면 in으로 바꿔준다.
SELECT co.order_id, co.customer_id, c.customer_nm, co.product_id, co.order_price
  FROM customer_order co, customer c
 WHERE co.customer_id = c.customer_id
   AND co.product_id in (select product_id
						from product
                        )