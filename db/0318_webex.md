- JOIN 을 SubQuery로

  - ```mysql
    SELECT co.order_id, co.customer_id, c.customer_nm, 
           co.product_id, p.product_nm, co.order_price, p.product_price
      FROM customer_order co, customer c, product p
     WHERE co.customer_id = c.customer_id
       AND co.product_id = p.product_id
       AND p.product_price <= 1500;
    
    SELECT co.order_id, co.customer_id, c.customer_nm, co.product_id, co.order_price,
           ( SELECT p.product_nm FROM product p 
              where co.product_id = p.product_id
                and p.product_price <= 1500 ) product_nm,
            ( SELECT p.product_price FROM product p 
                  where co.product_id = p.product_id
                    and p.product_price <= 1500 ) product_price
      FROM customer_order co, customer c
     WHERE co.customer_id = c.customer_id; 
    
    
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
    ```

- view

  - read only

  - 지우거나 생성 밖에 안된다. (일부 내용 수정 X)

  - ```mysql
    create or replace view summary as
    SELECT t.countrycode,
           co.NAME co_name,
           t.name ci_name,
           t.population
    FROM   country co
           LEFT OUTER JOIN (SELECT countrycode, NAME, population
            FROM   city
            WHERE ( countrycode, population ) IN (SELECT countrycode, Max(population)
                                                  FROM   city
                                                  GROUP  BY countrycode)) t
                        ON co.code = t.countrycode; 
    -- 테이블로 만든 것이 아니라
    -- 쿼리 수행문을 저장하는 것
    ```

### 데이터 모델링



- 모델링이란?
  - 어떤 현상, 대상에 대한 기록, 모형
  - 추상화, 단순화
  - 보편적 규칙
  - 기억, 소통의 방식

- 데이터 품질
  - 데이터로서의 가치
  - 축적되는 데이터의 활용 가치가 하락한다면?
    - 정확도 하락 (왜 A 데이터가 다르지?)
    - 신뢰도 하락 (A 데이터가 맞는거야? 아님 B 데이터가 맞는거야?)
  - 데이터 구조의 문제로부터 발생
    - 중복 데이터 미정의
    - 데이터 정의 불충분
    - 동일 성격 데이터 미 통합에 따른 불일치

- 데이터 모델링의 3단계
  - 개념적
    - 업무 중심의 포괄적, 추상적 모델링
  - 논리적
    - 개념적 모델링의 결과로부터 key, 속성, 관계 파악, 표현
  - 물리적
    - 실제 DBMS에 적용, 성능, 저장용량 등 고려한 작업 수행

- 데이터 모델링 3요소
  - Things
    - 업무에 포함된 모델링의 대상
  - Attributes
    - Things가 갖는 특성들
  - Relationshp
    - Things들 사이의 관계

- 모델링의 표현
  - Entity Relation Diagram
  - 나중에 구글링 해보기
- 모델링의 표현
  - Entity Relation Diagram
  - 실선
    - Identifying
    - 한쪽의 키가 다른 테이블로 연결될 때 그 테이블의 PK일 때
  - 점선
    - Non-Identifying
    - 다른 테이블의 key가 그 테이블의 PK가 아닐 때

### 정규화

- 데이터 모델링의 과정
- Entity와 Entity 또는 Entity 내 Attribute 들 관계를 파악
- 중복 및 종속성 관련 비효율성 제거
- 1,2,3,4,5 차 정규화 과정 외 보이스-코드 정규화 등
  - 1차 정규화
    - 테이블의 컬럼이 원자값(Atomic Value, 하나의 값)을 갖도록 테이블을 분해하는 것
  - 2차 정규화
    - Key의 부분 종속성 분리하여 별도의 Entity 구성
  - 3차 정규화
    - 키가 아닌 다른 속성에 의존적인 속성은 별도의 entity 구성

- 연습 1
  - 고객번호* - 고객명
  - 상품 번호* - 계약 상품명
  - 계약 번호 *- 고객 번호 - 계약 상품 번호 - 계약일 - 계약 상태
- 연습 2
  - 학생 번호 *- 학생이름
  - 강의 번호* - 강의 명 - 교수 명 - 금액
  - 학생 번호* - 강의 번호* - 수강 상태 (멀티 키)

### 역 정규화

- 정규화의 기본 방향은 Entity의 분리
- 업무 성격 상 정규화의 결과로 분리된 Entity들을 조회 시, 많은 JOIN 발생 -> 성능 이슈
- 정규화의 기본 방향에 위배되지만, 성능 문제를 해결하고자 취하는 일련의 작업
- 모든 Entity 대상 (X), 조회 업무가 많은 Entity 우선
- 역 정규화 후, 성능 향상 확인 -> 원복도 고려

### Master (원장)

- 업무의 핵심 Entity
- 최신 상태 유지
- Master의 변동 사항은 별도의 이력 Entity 구성
- 고객 Entity, 계좌 Entity 등
- 많은 JOIN의 기준

### Transactional (거래)

- 행위 Entity
- 등록 삭제만 가능
- 수정 불가 -> 카드 거래
- 수정 가능 -> 주문

### History(이력)

- 주요 Entity 변경 사항 관리
- 등록만 가능
- 수정, 삭제 불가
- log 성 데이터 (시간에 따라 남기는)
  - 주요 분쟁의 근거

### DW

- Data Warehouse
- 분석 용도
- 시계열성 데이터
- 마감 후 데이터 이관



### OLTP vs OLAP

- On-Line Transactional Processing
  - 일반 업무
- On-Line Analytical Proceesing





















