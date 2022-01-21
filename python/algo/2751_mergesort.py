def merge_sort(arr, left, right, temp):
    mid = (left + right) // 2
    if left >= right:
        return
    merge_sort(arr, left, mid, temp)
    merge_sort(arr, mid + 1, right, temp)
    merge(arr, left, mid, right, temp)
    pass



def merge(arr, left, mid, right, temp):
    left_idx = left
    right_idx = mid + 1
    idx = left
    # temp = []
    # for i in arr:
    #     temp.append(0)
    while left_idx <= mid and right_idx <= right:
        if(arr[left_idx] <= arr[right_idx]):
            temp[idx] = arr[left_idx]
            idx += 1
            left_idx += 1
        else:
            temp[idx] = arr[right_idx]
            idx += 1
            right_idx += 1
    while left_idx <= mid:
        temp[idx] = arr[left_idx]
        idx += 1
        left_idx += 1
    while right_idx <= right:
        temp[idx] = arr[right_idx]
        idx += 1
        right_idx += 1
    for i in range(left, right+1):
        arr[i] = temp[i]
    
import sys
N = int(sys.stdin.readline())
arr = []
temp = []

for i in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)
    temp.append(0)
merge_sort(arr,0,len(arr)-1, temp)
for i in arr:
    print(i)