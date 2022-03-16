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