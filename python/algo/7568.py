def find_rank(arr):
    for i in arr:
        ranking = 1
        for j in arr:
            if i == j:
                continue
            if i[0] < j[0] and i[1] < j[1]:
                ranking +=1
        i[2] = ranking
    pass



N = int(input())
arr = []
for i in range(N):
    weight, height = map(int, input().split())
    rank = -1
    X = [weight, height, rank]
    arr.append(X)
find_rank(arr)
for i in range(N):
    print(arr[i][2], end = " ")

