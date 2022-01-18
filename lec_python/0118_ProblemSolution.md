## 0118_문제풀이

### Mutable & Immutable

```python
String, List, Tuple, Range, Set, Dictionary
immutable : String, Tuple, Range
Mutable : List, Set, Dictionary
```

### 홀수만 담기

```python
list_a = list(range(1, 51))
# list_b = a[0:-1:2]
list_b = list_a[::2]
```

### Dictionary 만들기

```python
a = {'John' : 19, 'Anna' : 17}
```

### 반복문으로 네모 출력

```python
n = 5
m = 9
for height in range(m):
    print('*' * n)
for height in range(m):
    for width in range(n):
        print('*', end = '')
    print()
```

### 조건 표현식

```python
# 참일 때 출력 {조건문} 거짓일 때 출력
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```

### 평균 구하기

```python
scores = [80, 89, 99, 83]
total = 0
length = 0
for score in scores:
    total += score
    length += 1
print(total / length)

print(sum(scores) / len(scores))
```

### N의 약수

```python
N = int(input())
for i in range(1, N+1):
    if N % i == 0:
        print(i, end = " ")
```

### 중간값 찾기

```python
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):	#i+1번째 하는 이유는 i번째까지 정렬되있기 때문
        # 가장 작은값 제일 왼쪽으로 넘기기
numbers_sorted = sorted(numbers)
length = 0
for i in numbers:
    length +=1
center = length // 2 #몫
print(numbers_sorted[center])
```

### 계단 만들기

```python
number = int(input())
for i in range (1, number+1):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
```

















