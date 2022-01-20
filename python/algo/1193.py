def find_num(n):
    sum_temp = 0
    temp = 1
    while True:
        if n <= sum_temp:
            break
        sum_temp += temp
        temp += 1
    total_num = temp
    
    x = sum_temp - n + 1
    y = temp - x
    if temp % 2 == 1:
        print(f"{y}/{x}")
    else:
        print(f"{x}/{y}")

N = int(input())
find_num(N)