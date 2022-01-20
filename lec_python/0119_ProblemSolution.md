### Built-in 함수

```python
#내장함수 5가지 이상 쓰세요
print()
sum()
min()
max()
len()
```

### 정중앙 문자

```python
# 정중앙 문자를 반환하는 함수
# 만약 문자열의 길이가 짝수라면 중앙의 2개를 반환
def get_middle_char(word):
    length = 0
    # 단어 전부 순회
    for i in word:
        # 한개씩 개수를 새어보자.
        length += 1
    # 정 중앙값
    center = length // 2
    # 만약 홀수라면
    if length % 2:
        result = word[center]
    # 만약 짝수라면
    else:
        result = word[center-1] + word[center]
        result = word[center-1:center+1]    #위와 동일하게 작동, 뒤에껀 포함안되는 거 까먹지 말자
    return result
print(get_middle_char('ssafy'))
print(get_middle_char('coding'))
```

### 위치 인자와 키워드 인자

```python
ssafy(name = '길동', '구미')
# 오류발생
# 앞에서 먼저 키워드 처리했기 때문에 뒤에것을 포지션으로 처리할 수 없다.
```

### 나의 반환 값은

```python
def my_func(a, b):
    c = a + b
    print(c)
result = my_func(3, 7)
# result에 저장된 값은 없다.
# None
```

### 가변 인자 리스트

```python
# 가변 인자 리스트
# 다수의 인자들을 한번에 받아 보자.
def my_avg(*args):
    total = 0
    args_num = 0
    for i in args:
        total += i
        args_num += 1
    return total/args_num

# *에 관하여
# 패킹 : 매개변수에 사용할 때 (함수 정의 부분)
# 언패킹 : 전달인자에 사용할 때 (함수 사용 시)
def test(list_a, list_b):
    print(list_a, list_b)

test(*[['first'], ['second']]) #리스트 하나를 언패킹해서 리스트 2개가 매개변수에 들어가게 됨
```

### List의 합 구하기

```python
# 인자는 리스트 하나
def list_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
```

### Dictionary로 이루어진 리스트의 값 구하기

```python
def dict_list_sum(arr):
    result = 0
    # 순회
    for info in arr:
        result += info['age'] #딕셔너리 내의 키 age의 값에 접근
    return result
print(dict_list_sum([{'name': 'kim', 'age' : 12},{'name' : 'lee', 'age':4}]))
```

### 2차원 List의 전체 합 구하기

```python
def all_list_sum(arr):
    total = 0
    #전체 리스트 순회
    for i in arr:
        #안쪽 리스트 순회
        for j in i:
            total += j
    return total
```





































