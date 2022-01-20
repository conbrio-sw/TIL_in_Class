def find_num_xy(arr):
    x1 = arr[0]
    y1 = arr[1]
    r1 = arr[2]
    x2 = arr[3]
    y2 = arr[4]
    r2 = arr[5]

    x12 = (x1-x2)
    y12 = (y1-y2)
    d = (x12**2 + y12**2)**0.5
    r_differ = abs(r1 - r2)
    r_sum = r1 + r2

    if (x1 == x2) and ( y1 == y2) and (r1 == r2):
        return -1
    if d < r_differ or d > r_sum:
        return 0
    if d == r_differ or d == r_sum:
        return 1
    else:
        return 2
T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    print(find_num_xy(arr))