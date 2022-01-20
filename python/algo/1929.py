def find_pn(N):
    count = 0

    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    if count == 2:
        return True
    return False

def print_pn(M, N):
    for i in range(M, N+1):
        if find_pn(i):
            print(i)




def prime_number(M, N):
    n = N+1
    sieve = [True] * (n)
    sieve[1] = False
    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    for i in range(M, N+1):
        if sieve[i] == True:
            print(i)

M, N = map(int, input().split())

prime_number(M, N)