def get_secret_word(arr):
    arr_trans = []
    for i in arr:
        arr_trans.append(chr(i))
    rst = ""
    for i in arr_trans:
        rst += i
    return rst
#print(get_secret_word([83, 115, 65, 102, 89])) # => 'SsAfy'


def get_secret_number(S):
    rst = 0
    for i in S:
        rst += ord(i)
    return rst
# print(get_secret_number('tom')) # => 336

def get_strong_word(s1, s2):
    s1_asc = get_secret_number(s1)
    s2_asc = get_secret_number(s2)
    if s1_asc > s2_asc:
        return s1
    else:
        return s2

print(get_strong_word('z', 'a')) # => 'z'
print(get_strong_word('tom', 'john')) # => 'john'