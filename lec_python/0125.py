# a = [5,4,3,2,1]

# b = sorted(a)
# print(a, b)
# c = a.sort()
# print(a, c)


# a = [1,2,3]
# b = ['a', 'b']

# print(a.append(b))
# # print(a)
# print(a.extend(b))
# print(a)

# a = [1, 2, 3, 4, 5]
# b = a

# a[2] = 5

# print(a)
# print(b)

def duplicated_letters(word):
    # 반환할 리스트
    rst = []
    # string 순회
    for char in word:
        # 해당 문자가 중복되어 있고
        if word.count(char) > 1:
            # 반환할 리스트에 포함이 안되있으면 리스트에 해당 문자 추가
            if char not in rst:
                rst.append(char)
    return rst
# a = duplicated_letters('apple') # => ['p']
# b = duplicated_letters('banana') # => ['a', 'n']
# print(a, b)

def low_and_up(word):
    # 반환할 문자열
    rst = ""
    # String 순회
    for idx, char in enumerate(word):
        # 해당인덱스가 짝수면 소문자
        if idx % 2 == 0:
            rst += char.lower()
        # 아니면 대문자
        else:
            rst += char.upper()
    return rst
# a = low_and_up('apple') # =>aPpLe
# b = low_and_up('banana')  # => bAnAnA
# print(a,b)
def lonely(arr):
    # 반환할 리스트
    rst = ['init']
    # 반환할 리스트의 마지막 인덱스 저장
    rst_idx = 0
    # arr 리스트 순회
    for i in arr:
        # 만약 리스트 요소가 반환할 리스트의 마지막 인덱스가 아니면 추가
        if i != rst[rst_idx]:
            rst.append(i)
            # 마지막 인덱스 값 1 증가
            rst_idx += 1
    # 초기에 넣어준 'init' 제거
    rst = rst[1:]
    return rst

a = lonely([1, 1, 3, 3, 0, 1, 1]) # => [1, 3, 0, 1]
b = lonely([4, 4, 4, 3, 3]) # => [4, 3]
print(a, b)
