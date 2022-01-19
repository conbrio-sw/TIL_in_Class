from random import choice


def check_group_word(S):
    arr = []
    for i in S:
        arr.append(i)
    #print(arr)
    x = 1
    for j in range(0, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[k] == arr[j]:
                if arr[k-1] == arr[k]:
                    continue
                x = 0
                break
    return x               

N = input()
total = 0
for i in range(N):
    S = input()
    total += check_group_word(S)
print(total)
