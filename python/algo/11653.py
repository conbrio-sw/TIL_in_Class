def find_soinsu(N):
    if N == 1:
        return
    temp = N
    while True:
        for i in range(2, N//2 + 1):
            if temp % i == 0:
                print(i)
                temp = temp // i
                break
        if find_pn(temp):
            print(temp)
            break

def find_pn(N):
    count = 0

    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    if count == 2:
        return True
    return False        

N = int(input())
find_soinsu(N)