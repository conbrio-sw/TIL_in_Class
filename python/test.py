import math
import sys
import keyword
from tkinter import N
# a = 3.14
# b = 3.12
# print(a-b)
# c = 0.02
# print(f"a-b = c ? : {a-b==c}")
# print(math.isclose(a-b,c))A
# f = sys.float_info.epsilon
# print(f"a-b = c ? : {abs(a-b-c)<=f}")
# pi = 3.1455111111111111111111111
# print(f'원주율은 {pi:0.3f}')
# b = (1,2)
n = 5
m = 9
#답
#답
print('''
"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."
나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'
''')
# print(dictA[b])
# print(dictA)
# str1 = str(dictA)
# print(str1[1])

# a = 5 and 0
# print(a)

# a = 3   #integer
# b = '3' #string
# print(a)
# print(b)
# print(type(a), type(b))

# import keyword
# print(keyword.kwlist)

# num1 = 0.1 * 3 
# num2 = 0.3
# print(abs(num1-num2) <= sys.float_info.epsilon)
# print(math.isclose(num1, num2))

# name = '철수'
# print(f'안녕, {name}야')
# print('안녕, {}야'.format(name))
# print('안녕, %s야' % name)


# a = str(1)
# print(a)
# a = int('30')
# print(a)
# a =  int(5)
# print(a)
# a =  bool('50')
# print(a)
# a =  int('3.5')
# print(a)

# n = 5
# m = 9
# star = '*'
# star = star * 5 + '\n'
# star = star * 9
# print(star)

# a = float(input("2차항의 계수를 입력하세요: "))
# b = float(input("1차항의 계수를 입력하세요: "))
# c = float(input("상수항의 계수를 입력하세요: "))

# x1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
# x2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
# print(f"{x1}, {x2}")

# chars = input()

# for char in chars:
#     print(char)

# input_num = int(input())
# n = 1
# sum = 0
# while n <= input_num:
#     sum += n
#     n = n + 1

input_num = int(input())	#숫자입력한 것을 int형변환
n = 1
sum = 0
while n <= input_num:
    sum += n				#1부터 입력한 자연수까지 더하기
    n = n + 1				#종료조건 설정
print(sum)