def find_num_pn(args):
    count = 0
    for i in args:
        if find_pn(i):
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

N = int(input())
arr = list(map(int, input().split()))
find_num_pn(arr)