

N = int(input())
arr = []
for i in range(100000001):
    arr.append(0)

count = 0
for i in range(100000001):
    if '666' in str(i):
        count += 1
        arr[i] = count

for i in range(100000001):
    if arr[i] == N:
        print(i)
