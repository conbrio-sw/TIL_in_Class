## JOIN

- 둘 이상의 테이블에서 데이터가 필요한 경우 테이블 조인이 필요
- 일반적으로 조인 조건을 포함하는 WHERE 절을 작성해야한다
  - 테이블 갯수 - 1 개의 조인 조건이 필요
  - ON : 조인 조건
  - where : 일반 조건
- 조인 조건은 일반적으로 각 테이블의 PK 및 FK로 구성된다.
- 주의 사항
  - 조인의 처리는 어느 테이블을 먼저 읽을지를 결정하는 것이 중요
    - 처리할 작업량이 상당히 달라진다
  - INNER JOIN 
    - 어느 테이블을 먼저 읽어도 결과가 달라지지 않아 MySQL 옵티마이저가 조인의 순서를 조절해서 다양한 방법으로 최적화를 수행할 수 있다.
  - OUTER JOIN
    - 반드시 OUTER가 되는 테이블을 먼저 읽어야 하므로 옵티마이저가 조인 순서를 선택할 수 없다.

```mysql
select employee_id, first_name, salary, department_name
from employees, departments
where employees.department_id = departments.department_id
and employee_id = 100;
```

### INNER JOIN

```mysql
-- inner join
select e.employee_id, e.first_name, e.salary, e.department_name
from employees e inner join departments d
on e.department_id = d.department_id
where e.employee_id = 100;
```

- using

  ```mysql
  -- using
  select e.employee_id, e.first_name, e.salary, d.department_name
  from employees e inner join departments d
  using (department_id)
  where e.employee_id = 100;
  ```

- natural

  - 조건이 2개 겹쳐지면 이상하게 작동된다.

  ```mysql
  -- 부서번호가 10인 부서의 부서번호, 부서이름, 도시
  select d.department_id, d.department_name, l.city
  from locations l natural join departments d
  where d.department_id = 10;
  ```

### OUTER JOIN

- 어느 한쪽 테이블에는 해당하는 데이터가 존재하는데, 다른쪽 테이블에는 데이터가 존재하지 않을 경우, 그 데이터가 검색되지 않는 문제점을 해결하기 위해 사용

  - ```mysql
    select e.employee_id, e.first_name, d.department_name
    from employees e left outer join departments d
    on e.department_id = d.department_id;
    
    select d.department_id, d.department_name, e.employee_id, e.first_name
    from employees e right outer join departments d
    on e.department_id = d.department_id;
    ```

  - ```mysql
    select ifnull(d.department_name, '승진발령'), e.employee_id, e.first_name
    from employees e left outer join departments d
    on e.department_id = d.department_id
    union
    select d.department_name, e.employee_id, e.first_name
    from employees e right outer join departments d
    on e.department_id = d.department_id;
    
    -- union으로 full outer join 가능
    -- union all은 교집합을 빼지 않는다.
    -- minus -> 차집합인데 mysql에는 지원 x
    -- intersect -> 교집합
    ```

### SELF JOIN

- 같은 테이블끼리 JOIN

  ```mysql
  -- self join
  -- 모든 사원의 사번, 이름, 매니저사번, 매니저이름
  select e.employee_id, e.first_name, e.manager_id, m.first_name
  from employees e left outer join employees m
  on e.manager_id = m.employee_id;
  ```

### None-Equi JOIN

- 범위를 통해 join

- PK, FK가 아닌 일반 컬럼을 join 조건으로 지정

  ```mysql
  select e.employee_id, e.first_name, e.salary, s.grade
  from employees e join salgrades s
  where e.salary between s.losal and s.hisal;
  ```

- ```mysql
  -- 위의 정보를 출력 하였다면 위의 정보에 현재의 정보를 출력.
  -- 현재 근무이력의 시작일은 이전 근무이력의 종료일 + 1일로 설정.
  -- 종료일은 null로 설정.
  select jh.employee_id, e.first_name, d.department_name, j.job_title,
  date_format(jh.start_date, '%y.%m.%d'), date_format(jh.end_date, '%y.%m.%d')
  from job_history jh join departments d join employees e join jobs j
  on jh.department_id = d.department_id
  and e.employee_id = jh.employee_id
  and j.job_id = jh.job_id
  where jh.employee_id = 101
  union
  select e.employee_id,  e.first_name, d.department_name, j.job_title,
  date_format((select date_format(date_add(max(end_date), interval 1 day), '%y.%m.%d')
  from job_history jh
  where jh.employee_id = 101), '%y.%m.%d'), null
  from departments d join employees e join jobs j
  on e.department_id = d.department_id
  and e.job_id = j.job_id
  where e.employee_id = 101;
  
  -- 서브쿼리 맛보기
  ```

## SUBQUERY

- 다른 쿼리 내부에 포함되어 있는 SELECT 문을 의미
- 서브 쿼리를 포함하고 있는 쿼리를 외부 쿼리 또는 메인 쿼리라고 부르며, 서브 쿼리는 내부 쿼리라고 부른다
- 서브 쿼리는 비교 연산자의 오른쪽에 기술해야하고 반드시 () 로 감싸져있어야한다
- 종류
  - 중첩 서브 쿼리 WHERE 문에 작성하는 서브 쿼리
    - 단일 행
    - 복수(다중) 행
    - 다중 컬럼
  - 인라인 뷰 - FROM 문에 작성하는 서브 쿼리
  - 스칼라 서브 쿼리 - SELECT 문에 작성하는 서브 쿼리

- 주의사항

  - 반드시 ()로 감싸야한다
  - 단일 행 또는 다중 행 비교 연산자와 함게 사용된다.

- 사용가능한 곳

  - SELECT, FROM, WHERE, HAVING, ORERD BY, INSERT문의 VALUES, UPDATE문의 SET 등등

  ```mysql
  -- subquery
  select d.department_name
  from departments d
  where department_id = (select e.department_id
  						from employees e
  						where  e.employee_id = 100);
  ```

### Nested Subquery

- 단일행
  - 서브 쿼리의 결과가 단일행을 리턴

```mysql
-- where
-- ‘adam’과 같은 부서에 근무하는 사원의 사번, 이름, 부서번호.
select e.employee_id, e.first_name, e.department_id
from employees e
where department_id = (
						select department_id
                        from employees e
                        where first_name = 'adam'
						);
						
select e.employee_id, e.first_name, e.salary
from employees e
where e.salary > (
					select avg(salary)
                    from employees e
					)
order by 3 desc; -- 인덱스로 정렬 가능
```

- 다중행
  - 서브 쿼리의 결과가 다중행을 리턴 : IN, ANY, ALL

```mysql
-- any, all, in
-- 30번 부서에서 근무하는 모든(최대급여자보다) 사원들보다 급여를 많이 받는 사원의 사번, 이름, 급여, 부서번호.
-- 다중행 (all)
select employee_id, first_name, salary, department_id
from employees
where salary >  any (
				select salary
				from employees		
				where department_id = 30
				)
order by salary;

-- 모든 사원 중 적어도(최소급여자보다) 30번 부서에서 근무하는 사원의 급여보다 많이 받는 사원의 사번, 이름, 급여, 부서번호
-- 다중행 (any)
select employee_id, first_name, salary, department_id
from employees
where salary >  any (
				select salary
				from employees		
				where department_id = 30
				)
order by salary;

-- 근무 도시가 ‘seattle’(대소문자 구분X)인 사원의 사번, 이름.
-- 다중행 (in)
select employee_id, first_name
from employees
where department_id in (
					select department_id
					from departments
					where location_id = (
										select location_id
										from locations		
										where city = 'seattle'
										)
                    );
```

- 다중 열

  - 서브 쿼리의 결과가 다중열을 리턴

  ```mysql
  -- 다중열
  -- 커미션을 받는 사원중 매니저 사번이 148인 사원의 급여와 부서번호가 일치하는 사원의 사번, 이름
  select employee_id, first_name
  from employees
  where (salary, department_id) in (
  								select salary, department_id
  								from employees
  								where manager_id = 148
                                  and commission_pct is not null
  								);
  ```

### 인라인 뷰

- 인라인 뷰

  - FROM 절에 사용되는 서브 쿼리
  - 서브쿼리가 FROM절에 사용되면 뷰처럼 결과가 동적으로 생성된 테이블로 사용 가능
  - 임시적인 뷰이기 때문에 데이터베이스에는 저장되지 않음
  - 동적으로 생성된 테이블이기 때문에 컬럼을 자유롭게 참조가능

  - ```mysql
    -- 인라인뷰(Inline View)
    -- 모든 사원의 평균 급여보다 적게 받는 사원들과 같은 부서에서 근무하는 사원의 사번, 이름, 급여, 부서번호
    
    select avg(salary)
    from employees e;
    
    select e.employee_id, e.first_name, e.salary, e.department_id
    from (
    		select distinct department_id
            from employees
            where salary < (
    						select avg(salary)
    						from employees e
    						)
    		) d join employees e
    on d.department_id = e.department_id;
    ```

### 스칼러 서브 쿼리

- SELECT 절에 있는 서브 쿼리
- 한 개의 행만 반환

### 활용

- create

  - ```mysql
    create table emp_copy
    select *
    from employees;
    
    -- 내부 키 등도 전부 복사
    
    -- employees table의 구조만 emp_blank라는 이름으로 생성(컬럼 이름 동일).
    create table emp_blank
    select *
    from employees
    where 1 = 0;
    
    -- 50번 부서의 사번(eid), 이름(name), 급여(sal), 부서번호(did)만 emp50이라는 이름으로 생성.
    
    create table emp50
    select employee_id eid, first_name name, salary sal, department_id did
    from employees
    where department_id = 50;
    ```

- Insert

  - ```mysql
    -- 서브쿼리를 이용한 insert.
    -- employees table에서 부서번호가 80인 사원의 모든 정보를 emp_blank에 insert
    insert into emp_blank
    select *
    from employees
    where department_id = 80;
    
    -- 행을 맞춰야한다.
    -- 제약 조건도 잘 맞춰줘야한다.
    ```

- Update

  - ```mysql
    -- 서브쿼리를 이용한 update.
    -- employees table의 모든 사원의 평균 급여보다 적게 받는 emp50 table의 사원의 급여를 500 인상.
    update emp50
    set sal = sal + 500
    where sal < (select avg(salary) from employees);
    ```

- delete

  - ```mysql
    delete from emp50
    where sal < (select avg(salary) from employees);
    ```

  - 

















