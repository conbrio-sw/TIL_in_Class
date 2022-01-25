### Built-in 함수와 메서드

```python
#sorted(), .sort()의 차이점

#.sort() 매서드는 원본 리스트를 정렬하고 반환값이 없다.
#sorted() 함수의 경우는 정렬된 새로운 리스트를 반환한다.
```

### .extend()와 .append() 

```python
# .extend() 매서드의 경우, 인자로 들어온 순회 가능한 객체 순회해서 그 요소 하나하나를 리스트에 추가
# .append() 매서드의 경우, 인자 자체를 리스트에 추가
```

### 제대로 복사가 됐을까?

```python
a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a, b) #a[2], b[2] 동일하게 5로 바뀜

b = a[:] # shallow copy
import copy
b = copy.deepcopy(a)
```

### 중복된 글자들 찾아서 리스트에 담아서 반환

```python
def duplicated_letters(word):
    result = []
    # 중복된 글자?
    # count 매서드 사용
    for char in word:
        # 각 알파벳이 단어에 2번 이상 있다면
        if word.count(char) >= 2:
            if char not in result:
                result.append(char)
    # 순서 상관 없을 때 이래도 ㅇㅋ
    return list(set(result))
```

### 소대소대

```python
def low_and_up(word):
    rst = ''
    for idx, char in enumerate(word):
        if idx % 2 == 1:
            rst += char.upper()
        else:
            rst += char.lower()
     return rst
```

### 솔로 천국 만들기

```python
def lonely(numbers):
    result = [numbers[0]]
    for number in numbers:
        if result[-1] != number:
            result.append(number)
    return result
```





































