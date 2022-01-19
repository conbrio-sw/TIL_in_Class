A, B = map(int, input().split())

a_1 = A % 10
a_10 = (A // 10) % 10
a_100 = (A // 100) % 10
a_1, a_100 = a_100, a_1

A_new = a_100 * 100 + a_10 * 10 + a_1

b_1 = B % 10
b_10 = (B // 10) % 10
b_100 = (B // 100) % 10
b_1, b_100 = b_100, b_1
B_new = b_100 * 100 + b_10 * 10 + b_1

if A_new > B_new:
    print(A_new)
else:
    print(B_new)