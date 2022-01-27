### Circle 인스턴스 만들기

```python
class Circle:
    pi = 3.14
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
        
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
```

```python
circle = Circle(3, 2, 4)
print(circle.area())
print(circle.circumference)
```

### Dog와 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
```

```python
class Dog(Animal):
    def walk(self):
        print(f'{self,name}! 달린다!')
    def bark(self):
        print(f'{self.name}! 짖는다!')
class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')
```

### 오류의 종류

```
ZeroDivisionError : 0으로 나누려고 할 때
NameError : 정의되지 않은 변수 이름 사용
TypeError : 자료형에 대한 잘못된 사용
	ex) int(['123'])
IndexError : index 범위를 초과해서 조회하고자 할 때
KeyError : 딕셔너리에 없는 키를 조회하고자 할 때, 혹은 세트에 없는 값 삭제하거나 조회하려고 할 때
ModuleNotFoundError : 해당 모듈이 찾을 수 없을 때
ImportError : 모듈은 있는데 모듈에 없는 변수/클래스/함수를 찾고자 할 때
```



### pip

```bash
$ pip install faker
```

- faker라는 패키지를 설치하기 위한 명령어
- git bash에서 실행하는 명령어

### Basic Usages

```python
from faker import Faker # 1 ____ 을 하기 위한 코드이다.
fake = Faker() 			# 2 Faker는 ____, fake는 _____이다.
fake.name()				# 3 name()은 fake의 ____이다.
```

- Faker 클래스를 faker 패키지에서 불러온다.
- Faker는 클래스, fake 인스턴스 생성
- name()은 fake의 메서드

### Localization

```python
#인자 없이 호출 시에는 영문이 기본 설정이다. (en_US)
fake = Faker()
fake.name()
# => 'Shelly Wilcox' (랜덤이므로 결과 값이 다를 수 있음)

#Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.
fake_ko = Faker('ko_KR')
fake_ko.name()
# => '박진우' (랜덤이므로 결과 값이 다를 수 있음)
```

```python
class Faker():
    
    def __(a)__((b), (c)):
        pass
```

- `__init__`
- self
- locale = 'en_US'

### Seeding the Generator

```python
fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name()) 	# 1

fake2 = Faker('ko_KR')
print(fake2.name())	# 2
```



```python
fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name())	# 1

fake2 = Faker('ko_KR')
print(fake2.name())	# 2
```



- seed : 클래스 메서드
- seed_instance : 인스턴스 메서드



























