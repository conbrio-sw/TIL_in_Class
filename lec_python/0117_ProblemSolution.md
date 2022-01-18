## 0117_문제풀이

### 파이썬 예약어

```python
import keyword
print(keyword.kwlist)
# 여기에 나오는 애들
```

### 실수비교

```python
num1 = 0.1 * 3
num2 = 0.3
import math
math.isclose(num1, num2)
```

### 이스케이프 시퀀스

```python
\n	#줄 바꿈
\t	#탭
\\	#백 슬래시
```

### String Interpolation

```python
name = '철수'
print(f'안녕, {name}야')
print('안녕, {}야'.format(name))
#안녕, 철수야 출력
```

### 형변환

```python
int('3.5')	#ValueError발생
```

### 네모출력

```python
n = 5
m = 9
star = '*' * n + '\n'
print(star*m)
```

### 이스케이프 시퀀스 응용

```python
" ''  "	#출력가능
' ""  '	#출력가능
\"
\'
\\	#이스케이프 시퀀스 활용
```

### 근의공식

```python
(-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
(-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
```

```python
# 1을 값으로 갖는 튜플 a를 생성하시오.
a = (1, )	# 괄호 1인지, 튜플 1인지 확인할 수 없기 때문에 반드시 콤마를 찍어야한다.
b = [1]
c = {1}
```

### 세로로 출력하기

```python
input_num = int(input())
n = 1
while n <= input_num:
    print(n)
    n += 1
for i in range(1, input_num + 1):
    print(i)
```

### 거꾸로 세로로 출력하기

```python
input_num = int(input())
for i in range(input_num, -1, -1):
    print(i)
```

### N줄 덧셈

```python
input_num = int(input())
sum = 0
for i in range(1, input_num + 1):
    sum += i
print(sum)
```











