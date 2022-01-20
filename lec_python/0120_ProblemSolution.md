### all(), any()

- all(A + 0) = True이면 (편의상 0 = 공집합)

- all(A) = True 이기 때문에

- all(0) = True 여야만 한다.

- any(A + 0) = False이면

- any(A) = False 이기 때문에

- any(0) = False

  

### 이름공간

```python
Local
Enclosed
Global
Built-in
```

### 매개변수와 인자 그리고 반환

```python
return a, b
# 가능하다
# 튜플로 반환 가능
```

### 재귀함수

```python
자기 자신을 호출하는 재귀함수는 주로 알고리즘 문제를 구현할 시 많이 사용한다.
코드가 더 직관적, 이해하기 쉽다 (구현 자체는 어렵다)
재귀함수의 경우 함수가 호출될 때 마다 메모리 공간에 함수가 쌓여나가는 것을 확인할 수 있다
	=>	메모리 스택이 넘치는 형상(stack overflow)
    =>	이런 상황을 방지하고자, 파이썬에서는 기본적으로 1000번이 넘어가게 되면 더 이상 함수를 호출하지 않		고 종료
```

### 숫자의 의미

```python
def get_secret_word(arr):
    # 최종 반환 할 값
    result = ''
    # 전체 리스트 순회
    for i in arr:
        # 각 요소들 -> 정수를 문자열로 변환
        # result에 더해 나간다
        result += chr(i)
   	return result
```

### 내 이름은 몇일까?

```python
def get_secret_number(word):
    result = 0
    for i in word:
        result += ord(i)
    return result
```

### 강한 이름

```python
def get_strong_word(s1, s2):
    s1_asc = get_secret_number(s1)
    s2_asc = get_secret_number(s2)
    s1_asc = 0
    s2_asc = 0
    for char in s1:
        s1_asc += ord(char)
    for char in s2:
        s2_asc += ord(char)
    if s1_asc > s2_asc:
        return s1
    else:
        return s2
```

