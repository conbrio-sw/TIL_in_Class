# H,M = map(int, input().split())
# if M > 45:
#     print(H, M - 45)
# else:
#     if H == 0:
#         print(23, M + 15)
#     else:
#         print(H-1, M + 15)

# N = int(input())

# origin = N
# count = 0
# while True:
#     count += 1
#     N = (N // 10) + (N % 10) + (10* (N % 10))
#     if N == origin:
#         break
# print(count)

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(9):
#     a = int(input())
#     A[i] = a
# max_idx = 0
# max = A[0]
# for i in range(9):
#     if A[i] > max:
#         max = A[i]
#         max_idx = i
# print(max)
# print(max_idx)

# A = int(input())
# B = int(input())
# C = int(input())
# A, B, C = 150, 266, 427
# rstt = A * B * C
# print(rstt)
# for i in range(10):
#     count = 0
#     rst = rstt
#     while True:
#         if rst % 10 == i:
#             count += 1
#         if rst < 10:
#             break
#         rst = rst // 10
#     print(count)
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in range(11):
#     a = int(input())
#     A[i] = a
# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# for i in range(11):
#     B[i] = A[i] % 42
# B_set = set(B)
# print(len(B_set))
# import sys
# N = int(input())
# A = list(map(int, sys.stdin.readline().split()))
# total = 0
# maxA = max(A)
# for i in A:
#     if i < maxA:
#         C = i / maxA * 100
#     else:
#         C = i
#     total += C
# print(total/N)
# N = int(input())
# for i in range(N):
#     ox = input()
#     score = 0
#     o_num = 0
#     for j in ox:
#         if j == '0':
#             o_num += 1
#             score += o_num
#         else:
#             o_num =  0
#     print(score)
# C = int(input())
# for i in range(C):
#     N, *A = map(int, input().split())
#     print(A)
#     avg = sum(A)/len(A)
#     count = 0
#     for j in A:
#         if j > avg:
#             count += 1
#     ptg = 100 * count / len(A)
#     print(f'{ptg:.3f}%')

listA = []
for i in range(1, 10000):
    num = i
    temp = i
    while True:
        num += (temp % 10)
        if temp < 10:
            break
        temp = temp // 10
    listA.append(num)
#print (listA)
for i in range(1, 10000):
    if i in listA:
        continue
    print(i)