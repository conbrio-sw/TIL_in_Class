# def countingsort(arr, temp):
#     # temp = []
#     # for i in range(0, 10001):
#     #     temp.append(0)
#     # for i in arr:
#     #     temp[i] += 1
#     # for i in range(0, 10001):
#     #     while temp[i] > 0:
#     #         print(i)
#     #         temp[i] -=1
#     abc = sorted(temp.keys())
#     for i in abc:
#         while temp[i] > 0:
#             print(i)
#             temp[i] -= 1

# N = int(input())
# arr = []
# temp = {}

# # tempp = []
# # for i in range(0, 100001):
# #     tempp.append(0)
# for i in range(N):
#     n = int(input())
#     arr.append(n)
#     if n in temp.keys():
#         temp[n] += 1
#     else:
#         temp[n] = 1
# # print(temp)
# countingsort(arr, temp)
# # print(temp.keys())



def countingsort(arr, temp):
    for i in range(0, 10001):
        while temp[i] > 0:
            print(i)
            temp[i] -=1
N = int(input())
arr = []
temp = []
for i in range(0, 10001):
    temp.append(0)
for i in range(N):
    n = int(input())
    arr.append(n)
    temp[n] += 1
for i in range(0, 10001):
        while temp[i] > 0:
            print(i)
            temp[i] -=1
# countingsort(arr, temp)