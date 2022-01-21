from audioop import minmax
from ipaddress import summarize_address_range
import math
from threading import local
num1 = 0.1 * 3
num2 = 0.3
very_small_value = 10E-10
# print(f'일반비교 : {num1 == num2}')

# print(f'math 사용 : {math.isclose(num1, num2)}')

# print(f'작은 수랑 비교 : {abs(num1 - num2) <= very_small_value}')

# name = '철수'

# print(f'안녕, {name}야')
# print('안녕, {}야'.format(name))
# print('안녕, %s야' %name)

# print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')

# a, b, c = 1, 1, 1
# x, y = (-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a)
# n = 5
# m = 9
# star = '*'*n + '\n'
# star *= m
# print(star)
# number = int(input())

# for i in range(1, number + 1):
#     print(i)

# for i in range(number, -1, -1):
#     print(i)

# total = 0
# for i in range(1, number + 1):
#     total += i
# print(total)

#mutable : List, Set, Dict
#immutable : String, Tuple, Range

# list1 = list(range(1, 51))
# list2 = list1[::2]
# print(list2)

# dict1 = {'강현준' : 27}
# print(dict1, type(dict1))

# n = 5
# m = 9
# for i in range(m):
#     for i in range(n):
#         print('*', end="")
#     print()
# temp = 361.5
# print('입실불가') if temp >= 37.5 else print('입실가능')

# A = [80, 89, 99, 83]
# length = 0
# total = 0
# for i in A:
#     total += i
#     length += 1
# print(total/length)

# N = int(input())

# for i in range(1, N+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# def get_middle_char(S):
#     length = 0
#     for i in S:
#         length += 1
#     center = length // 2

#     if length % 2 == 1:
#         return S[center]
#     else:
#         return S[center-1] + S[center]

# print(get_middle_char('ssafy'))
# print(get_middle_char('coding'))

# def my_avg(*args):
#     length = 0
#     total = 0
#     for i in args:
#         length += 1
#         total += i
#     return total / length

# print(my_avg(77, 83, 95, 80, 70))

# def all_list_sum(arr):
#     total = 0
#     for i in arr:
#         for j in i:
#             total += j
#     return total
# print(all_list_sum([[1], [2,3], [4,5,6], [7,8,9,10]]))

#local
#Enclosed
#global
#built-in

def get_secret_word(arr):
    s = ''
    for i in arr:
        s += chr(i)
    print(s)
    return s
get_secret_word([83, 115, 65, 102, 89])

def get_secret_number(arr):
    s = 0
    for i in arr:
        s += ord(i)
    print(s)
    return s
get_secret_number('tom')

def get_strong_word(arr1, arr2):
    arr1_rst = 0
    arr2_rst = 0
    for i in arr1:
        arr1_rst += ord(i)
    for i in arr2:
        arr2_rst += ord(i)
    if arr1_rst > arr2_rst:
        return arr1
    else:
        return arr2
print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))