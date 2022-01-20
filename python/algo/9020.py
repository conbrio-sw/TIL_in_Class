def goldbh(n):
    N = n + 1
    arr = [True] * N
    arr[1] = False
    m = int(N ** 0.5)
    for i in range(2, m):
        if arr[i] == True:
            for j in range(i + i, N, i):
                arr[j] = False
    x = 0
    y = 0
    for i in range(int(n/2), N):
        if arr[i] == True:
            if arr[n-i] == True:
                x = i
                y = n-i
                break
    print(y, x)






T = int(input())
for i in range(T):
    C = int(input())
    goldbh(C)