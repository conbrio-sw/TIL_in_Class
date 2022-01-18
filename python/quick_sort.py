from sys import base_prefix


def quick_sort(arr, start, end):
    # 리스트에 남은 것에 1개 이하일 때 리턴
    if start >= end:
        return
    # 피벗은 가장 왼쪽 인덱스의 값으로 설정
    pivot = start
    left = start + 1
    right = end

    
    # left와 right가 같을 때 까지만...
    while(left <= right):
        # 왼쪽부터 시작하는 인덱스 중 피벗보다 큰 것을 찾을 때 까지 +1
        while(left <= end and arr[left] <= arr[pivot]):
        #while(arr[left] <= arr[pivot] and left <= end): ## 무조건 left end 먼저 비교...
            left += 1
        # 오른쪽부터 시작하는 인덱스 중 피벗보다 작은 것을 찾을 때 까지 -1
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        # 교차가 되었다면, 모든 탐색이 끝났다는 의미기 때문에 피벗 제 위치에 집어넣기
        if(left > right):
            arr[pivot], arr[right] = arr[right], arr[pivot]
        # 교차가 되지 않았다면, 서로 교환
        else:
            arr[left], arr[right] = arr[right], arr[left]

    pivot_index = right

    # 분할정복
    quick_sort(arr, start, pivot_index-1)
    quick_sort(arr, pivot_index + 1, end)

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

