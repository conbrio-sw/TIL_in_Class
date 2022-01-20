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

M = int(input())
N = int(input())

total = 0
min_value_TF = True
min_value = 0
for i in range(M, N+1):
    if find_pn(i):
        total += i
        if min_value_TF:
            min_value = i
            min_value_TF = False
if min_value_TF:
    print(-1)
else:
    print(total)
    print(min_value)