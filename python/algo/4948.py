def find_numPN(n):
    M = 2*n + 1
    arr = [True] * M
    m = int(M ** 0.5)
    arr[1] = False
    for i in range(2, m + 1):
        if arr[i] == True:
            for j in range(i+i, M, i):
                arr[j] = False
    count = 0
    for i in range(n+1, M):
        if arr[i] == True:
            count += 1
    print(count)

while True:
    n = int(input())
    if n == 0:
        break
    find_numPN(n)
