### 모음은 몇 개 일까?

```python
def count_vowels(word):
    count = 0
    vowels = 'aeiou'
    # 모음리스트를 돈다.
    for vowel in vowles:
        # word에 해당모음의 갯수만큼 반환할 count 값을 더해준다.
        count += word.count(vower)
    return count
```



### 문자열 조작

```python
.strip([chars]) : 특정 문자를 지정하지 않으면 공백을 제거.
```

### 정사각형의 넓이만 출력

```python
def only_square_area(widths, heights):
    # 반환할 리스트
    rst = []
    for width in widths:
        for height in heights:
            if width == height:
                rst.append(width*height)
    return rst

	# 리스트 컴프리헨션 방법
    # 리스트에 최종적으로 추가 할 값 + 반복문 순서대로 + 조건
    result = [width * heigt for width in widths for height in heights if width == heigth]
    
    value = set(width) & set(heights)
    for val in value:
        rst.append(val**2)
    return rst
```

### 전체 과목 점수의 평균

```python
def get_dict_avg(score):
    rst = 0
    length = 0
    for score in scores:
        length += 1
        rst += score
    return rst / length
```

### 혈액형 분류하기

```python
def count_blood(blood):
    # 반환할 딕셔너리
    rst = {}
    # 리스트 반복문 돌리기
    for val in blood:
        # rst에 해당하는 키값이 있다면 +1
        # 값이 없더라도 키 에러가 발생하지 않도록
        if rst.get(val):
            rst[val] += 1
        # 없다면 최초로 할당
        else:
            rst[val] = 1
      
    rst = {}
    for key in blood:
        rst[key] = rst.get(key, 0) + 1
    return result
```

