from operator import rshift


def get_dict_avg(dict):
    pass
    # 전체 값, 갯수 0
    total = 0
    length = 0
    # dict 객체 돌면서 value값 더해주기
    for i in dict.values():
        length += 1
        total += i
    return total / length




# a = get_dict_avg({
#     'python': 80,
#     'algorithm': 90,
#     'django': 89,
#     'web': 83,
# })
# print(a)

def count_blood(ABO):
    pass
    # 반환할 rst 초기화
    rst = {}
    # 리스트 탐색하기
    for i in ABO:
        # 이미 존재한 혈액형이면 해당 혈액형 value 1 증가
        if i in rst.keys():
            rst[i] += 1
        # 없으면 해당 혈액형 만들어주기
        else:
            rst[i] = 1
    return rst


# abo_dict = count_blood([
#     'A', 'B', 'A', 'O', 'AB', 'AB',
#     'O', 'A', 'B', 'O', 'B', 'AB',
# ])
# print(abo_dict)

def count_vowels(word):
    rst = 0
    rst += word.count('a')
    rst += word.count('e')
    rst += word.count('i')
    rst += word.count('o')
    rst += word.count('u')
    return rst
    

# a = count_vowels('apple')
# b = count_vowels('banana')
# print(a, b)

def only_square_area(widths, heights):
    pass
    # 반환할 리스트 만들기
    rst = []
    # 넓이 하나 골라주기
    for i in widths:
        # 고른 넓이와 같은 값을 가지는 높이가 있다면
        # 곱해주기
        if i in heights:
            rst.append(i*i)
    return rst


# a = only_square_area([32, 55, 63], [13, 32, 40, 55])
# print(a)

# a = {'1' : 'a', '2' : 'b'}
# print(a.get('1'))

# str1 = 'apple'
# print(str1)

# str2 = ' a a a a a a a a '
# print(str2.replace(' ', ''))
# str3 = 'abc'
# print(list(str3))

dict1 = {1 : 'a', 'f' : 'abc'}
dict1.update([1, 'aa'])
print(dict1)