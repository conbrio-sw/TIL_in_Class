# HW

# 정중앙 문자를 반환하는 함수
# 만약 문자열의 길이가 짝수라면 중앙의 2개를 반환
import ssl


def get_middle_char(word):
    length = 0
    # 단어 전부 순회
    for i in word:
        # 한개씩 개수를 새어보자.
        length += 1
    # 정 중앙값
    center = length // 2
    # 만약 홀수라면
    if length % 2:
        result = word[center]
    # 만약 짝수라면
    else:
        result = word[center-1] + word[center]
        result = word[center-1:center+1]    #위와 동일하게 작동, 뒤에껀 포함안되는 거 까먹지 말자
    return result
# print(get_middle_char('ssafy'))
# print(get_middle_char('coding'))

# 가변 인자 리스트
# 다수의 인자들을 한번에 받아 보자.
def my_avg(*args):
    total = 0
    args_num = 0
    for i in args:
        total += i
        args_num += 1
    return total/args_num
# print(my_avg(77, 83, 95, 80, 70))
# 추가 개념
def test(list_a, list_b):
    print(list_a, list_b)
# test(*[['first'], ['second']])

# WorkShop

# 인자는 리스트 하나
def list_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
# print(list_sum([1,2,3,4,5]))

#Dictionary로 이루어진 리스트의 값 구하기
def dict_list_sum(arr):
    result = 0
    # 순회
    for info in arr:
        result += info['age']
    return result
#print(dict_list_sum([{'name': 'kim', 'age' : 12},{'name' : 'lee', 'age':4}]))

# 2차원 List의 전체 합 구하기
def all_list_sum(arr):
    total = 0
    #전체 리스트 순회
    for i in arr:
        #안쪽 리스트 순회
        for j in i:
            total += j
    return total

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))
# numbers = [ [0,1,2,2,2,2,2,2,2,2,2,2,2],
#             [3,4,5,5,5,5,5,5,5,5,5,5,5],
#             [6,7,8]]
# from pprint import pprint
# pprint(numbers)
print(sum([[1],[2,3],[4,5,6],[7,8,9,10]],[]))

print(type(3+4j))
print(type(3+4j) == complex)
a = 3+4j
print(a.real, a.imag)

rst = (a.real**2 + a.imag**2)**0.5

a = "z"
b = a + a
print(b)

