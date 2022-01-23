## 1차 시험 대비

### 파이썬 예약어

```python
import keyword
print(keyword.kwlist)
# 여기 찍힌 애들이 다 예약어
```

### 문자열 슬라이싱

```python
#만약 len = 10인 list가 있다면
A[9] = A[-1]
A[center] + A[center+1] = A[center:center+2]
```

### 날짜형식 출력

```python
import datetime
today = datetime.datetime.now()
print(today) # 2022-01-23 07:45:19.912978
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}') # 오늘은 22년 01월 23일 Sunday
type(today) # datetime.datetime
```

### 패킹, 언패킹

- 패킹되면 list로 대입된다.
- 언패킹되면 튜플 형태로 돼입된다.

```python
x, *y = 1, 2, 3, 4
type(x)	# int
type(y)	# list => [2, 3, 4]
===============================
def multiply(x, y, z):
    return x * y * z
numbers = [1, 2, 3]
multiply(*numbers)	# 6 ==>> numbers 는 항상 3개만 갖고 있어야한다.
```

### 세트(Set)

```python
set_a = {1, 2, 3}
set_b = {3, 6, 9}
print(set_a - set_b)	# 차집합, {1, 2}
print(set_a | set_b)	# 합집합, {1, 2, 3, 6, 9}
print(set_a & set_b)	# 교집합, {1}
```

### for - else

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.') # b가 없습니다.

for char in 'banana':
    if char == 'b':
        print('b!')		#b! 출력
        break
else:
    print('b가 없습니다.') #출력 안됨
```

### 함수 정의, 호출 시 주의사항

```python
def greeting(name='john', age):
    return f'{name}은 {age}살입니다.'
# 오류발생
# non-default argument follows default argument
greeting(age=24, '철수')
# 오류발생
# positional argument follows keyword argument
```

### 여러개 인자 처리

```python
def my_max(*args):			#가변 인자 리스트
    result = args[0]		# args의 타입은 튜플
    for value in args:
        if value > result:
            result = value
    return result

def my_dict(**kwargs):		#가변 키워드 인자
    return kwargs			#kwargs의 타입은 딕셔너리
print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')) 
# {'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
```

### map

```python
numbers = ['1', '2', '3']
new_numbers = [int(num) for num in numbers]
new_numbers = list(map(int, numbers))
```

### filter

```python
def odd(n):
    return n % 2
numbers = [1, 2, 3]
new_numbers = list(filter(odd, numbers))
new_numbers = [num for num in numbers if odd(n)]
a = list(filter(lambda x : x % 2, numbers))
```



### 찔끔찔끔

```python
True + 3 # 4 =>> True는 1로 인식한다. 숫자 데이터랑 연산할때

print(divmod(5, 2))
quotient, remainder = divmod(5, 2)
print(f'몫은 {quotient}, 나머지는 {remainder}') # 몫은 2, 나머지는 1

print('0 보다 큼') if num > 0 else print('0 보다 크지않음') # 조건표현식 사용법

cublic_list = [number**3 for num in range(1,4)] # [1, 8, 27]
cubic = {number: number ** 3 for number in range(1, 4)} # {1: 1, 2: 8, 3: 27}

dir(__builtins__)	# 내장함수 보는 방법

print('다섯번째 문장', '마지막 문장', sep='/', end='끝!') #다섯번째 문장/마지막 문장끝!
```

















































