### Type Class

```python
int, float, complex, str, list, dict, map, zip ...

# 내장 클래스들
```

### Magic Method

```python
# __init__	: 생성자 (인스턴스가 생성할 때 실행)
# __del__ 	: 소멸자 (인스턴스가 소멸될 때 실행)
# __str__	: 사람이 보기 좋게 출력
#			: str(Object), format(), print()에 의해서 호출되는 방식
# __repr__	: 기계(개발자)가 보기 좋게 출력
#			: 디버깅에 사용되기 때문에, 조금 더 많은 정보를 담은 형태로 출력
```

### Instance Method

```python
list : append, pop, remove
str : split, join, lower
dict : get, update
```

### Module Import

```python
# fibo.py
def fibo_recursion(n):
    pass
```

```python
# 같은 경로일 때
from fibo import fibo_recursion as recursion

recursion(4)
```



### 도형만들기

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.width = abs(self.p1.x - self.p2.x)
        self.height = abs(self.p1.y - self.p2.y)
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
```

