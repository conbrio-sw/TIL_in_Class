# from fibo import fibo_recursion as recursion
# from faker import Faker
# fake = Faker()
# print(fake.name())
# print(type(fake))


class Point:

    # 생성자
    def __init__(self, x, y):
        # 인스턴스 변수
        self.x = x
        self.y = y

class Rectangle:

    # 생성자
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        width = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return width * height
    
    def get_perimeter(self):
        width = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return 2*(width + height)
    
    def is_square(self):
        width = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return width == height

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())