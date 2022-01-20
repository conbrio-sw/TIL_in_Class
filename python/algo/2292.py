def number_of_room(n):
    if n == 1:
        return 1
    count = 1
    min_n = 2
    max_n = 7
    d = 6
    while True:
        if min_n <= n <= max_n:
            count += 1
            break
        min_n = max_n + 1
        d += 6
        max_n += d
        count += 1
    return count

N = int(input())
print(number_of_room(N))
