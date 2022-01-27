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

# c1 = Circle(3, 2, 4)
# print(f"둘레: {c1.circumference():.2f}, 넓이: {c1.area():.2f}")

class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
# Animal 상속
class Dog(Animal):
    # bark() 메서드 추가 구현
    def bark(self):
        print(f'{self.name}! 짖는다!')
    # walk() 오버라이딩
    def walk(self):
         print(f'{self.name}! 달린다!')
# Animal 상속
class Bird(Animal):
    #fly만 추가 구현
    def fly(self):
        print(f'{self.name}! 푸드덕!')

# dog = Dog('멍멍이')
# dog.walk() # 멍멍이! 달린다!
# dog.bark() # 멍멍이! 짖는다!

# bird = Bird('구구')
# bird.walk() # 구구! 걷는다!
# bird.eat() # 구구! 먹는다!
# bird.fly() # 구구! 푸드덕!

import random

random.random() # => 임의의 수
random.random() # => 임의의 수

random.seed(7777)
random.random() # => 0.xxx

random.seed(7777)
random.random() # => 0.xxxx
from faker import Faker
fake = Faker('ko_KR')


print(fake.name()) 	# 1
Faker.seed(4321)
fake2 = Faker('ko_KR')
print(fake2.name())	# 2

# fake = Faker('ko_KR')
# fake.seed_instance(4321)

# print(fake.name())	# 1

# fake2 = Faker('ko_KR')
# print(fake2.name())	# 2
# def dict_invert(my_dict):
#     rst = {}
#     for key, value in my_dict.items():
#         rst = {key : value}
#         print('zz', rst)
#     return rst
#     pass
# print(dict_invert({1: 10, 2: 20, 3: 30}))
# print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30}))
# print(dict_invert({1: True, 2: True, 3: True}))