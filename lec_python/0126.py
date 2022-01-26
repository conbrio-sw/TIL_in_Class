
# class 대문자로 시작하는 이름
class Person:
    # 클래스 속성
    __population = 0
    # 생성자
    # 특별한 데코레이터가 없는 메서드는
    # 인스턴스 메서드고,
    # 인스턴스의 속성을 혹은 값을 조작하는 행위를 위한 메서드
    # 첫 번쨰 인자로는 인스턴스 자신이 오게 될 것이다.
    # self라는 이름은 관례적인 것이고, 바뀌어도 문제는 없다.
    # 하지만 바꾸지는 않을 것이다.
    def __init__(self, name):
        # 인스턴스 속성
        self.name = name
        # 아래 코드는 클래스 내부의 population을 증가 못 시킨다.
        # self.population += 1
        # 아래는 되긴 된다.
        # 근데 이렇게 하면 바깥에서 아래 코드를 쓴거나 다름없다.
        # Person.population += 1
        self.increase()
    @classmethod
    def increase(cls):
        cls.__population += 1
        print(cls.__population)
    @classmethod
    def print_population(cls):
        print(cls.__population)
class Human(Person):
    pass
# kim = Person('김구현')
# # kim 인스턴스는 name 속성을 처음 생성할 때 할당되어서 가지게 된다.
# # print("kim의 name : ", kim.name)
# # print("kim의 type : ", type(kim))
# Person.print_population()
# Human.print_population()
# print("=================================================")
# hong = Person('홍길동')
# # print("hong의 name : ", hong.name)
# # print("kim.population == hong.population? :", kim.population == hong.population)
# # # kim.population을 바꿔도 클래스 population은 바뀌지 않는다.

# # # 클래스 메서드지만 인스턴스에서 호출 가능
# # # kim.increase()
# # # Person.increase()
# # print("kim.population, hong.population :", kim.population, hong.population)
# # c = Human('zz')
# # print(c.name)
# # print("kim.population, hong.population, Person.population, Human.population :", kim.population, hong.population,Person.population ,Human.population)
# c = Human('홍길동')

# Person.print_population()
# Human.print_population()
# print("===================================")
# d = Person('zzz')
# Person.print_population()
# Human.print_population()
# print("===================================")
# e = Person('zzz')
# Person.print_population()
# Human.print_population()
# print("===================================")
# print("===================================")
# print("===================================")
class SSAFY:
    __population = 0
    def __init__(self, name):
        self.name = name
        self.increase()
    @classmethod
    def increase(cls):
        cls.__population += 1
        print(cls.__population)
    @classmethod
    def print(cls):
        print(cls.__population)

class Python(SSAFY):
    pass
class JAVA(SSAFY):
    pass
a = SSAFY('a')
b = Python('b')
aa = SSAFY('aa')
c = JAVA('c')
print('=========================================')
SSAFY.print()
Python.print()
JAVA.print()
print('=========================================')
d = SSAFY('d')
SSAFY.print()
Python.print()
JAVA.print()

b = "zz"
print(Python.mro())