def find_numPN(n):
    count = 0
    for i in range(n, 2*n+1):
        if find_pn(i) == True:
            count += 1
    print(count)
def find_pn(N):
    count = 0

    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    if count == 2:
        return True
    return False

while True:
    n = int(input())
    if n == 0:
        break
    find_numPN(n)
