import sys
# 1. 산술평균
# 2. 중앙값
# 3. 최빈값, 여러개면 2번째로 작은 값
# 4. 범위를 출력




N = int(sys.stdin.readline())
# arr = []
# for i in range(N):
#     n = int(sys.stdin.readline())
#     arr.append(i)




#arr = [1, 3, 8, -2, 2]
arr1 = sorted(arr)
avg = sum(arr) / len(arr)
print(round(avg))
print(arr1[len(arr)//2])
max_appear = 0
max_appear_size = 1
max_appear_num = -4001
left = 0
right = 0
for i in range(0, len(arr1)-1):
    right = i
    if arr1[i] < arr[i+1]:
        this_appear = right - left + 1
        if this_appear > max_appear:
            max_appear = this_appear
            max_appear_size = 1
            max_appear_num = arr1[i]

        elif this_appear == max_appear:
            max_appear_size += 1
            if max_appear_size == 2:
                max_appear_num = arr1[i]


        left = i + 1

print(max_appear_num)
print(arr1[len(arr1)-1]-arr1[0])
