# 숫자를 받아서 (input)
# 세제곱 결과를 반환 (output)
def cube(n):
    return n ** 3

# print(cube(2))
# print(cube(100))

def rectangle(width, height):
    area = width * height
    round = 2*(width + height)
    return area, round

# print(rectangle(30, 20))

def add(*args):
    print(type(args))
    for arg in args:
        print(arg)
# add(2)
# add(2,3,4,5) 

# def family(**kwargs):
#     # for key, value in kwargs:
#     #     print(key, ":", value)
#     print(kwargs, type(kwargs), len(kwargs))
#     for i, x in kwargs.items():
#         print(i, x)
# family(father = 'john', mother = 'jane', me = 'john jr.')

# dicta = {'a' : 1, 'b' : 2, 'c' : 3}
# print(dicta, type(dicta), len(dicta))
# for i, x in enumerate(dicta):
#     print(i, x)

def abc(*args, a):
    print(args, a)

# abc(1,2,3)

def get_middle_char(strA):
    if len(strA) % 2 == 1:
        return strA[len(strA)//2]
    else:
        temp = strA[len(strA)//2-1] + strA[len(strA)//2]
        return temp
# print(get_middle_char('ssafy'))
# print(get_middle_char('coding'))
def ssafy(name, location = '서울'):
    print(f'{name}의 지역은 {location}입니다.')
# #(1)
# ssafy('허준')
# #(2)
# ssafy(location = '대전', name = '철수')
# #(3)
# ssafy('영희', location ='광주')
# #(4)
def my_func(a,b):
    c = a+b
    print(c)
# result = my_func(3, 7)
# print(result)

def my_avg(*args):
    cnt = 0
    total = 0
    for i in args:
        cnt += 1
        total += i
    return total/cnt

a = my_avg(77, 83, 95, 80, 70) #=> 81.0
# print(a)

def list_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

# print(list_sum([1, 2, 3, 4, 5]))
def dict_list_sum(arr):
    total = 0
    for i in arr:
        total += i['age']
    return total
a = dict_list_sum([{'name': 'kim', 'age':12}, {'name': 'lee', 'age' : 4}])
print(a)

def all_list_sum(*arr):
    total = 0
    for i in arr:
        for j in i:
            total += j
    return total
a = all_list_sum([1],[2,3],[4,5,6],[7,8,9,10])
print(a)