def find_min(N):
    kg_3 = 0
    kg_5 = 0
    kg_5_max = N // 5
    count = 0
    temp = N
    for i in range (kg_5_max, -1, -1):
        count = i
        temp = N - i*5
        if temp % 3 == 0:
            count += (temp // 3)
            return count
    return -1

N = int(input())
print(find_min(N))