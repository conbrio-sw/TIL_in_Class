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
        #while(arr[left] <= arr[pivot] and left <= end):
            left += 1
        # 오른쪽부터 시작하는 인덱스 중 피벗보다 작은 것을 찾을 때 까지 -1
        while(arr[right] >= arr[pivot] and right > start):
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


array=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def quick_sort1(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)

quick_sort1(array, 0, len(array) - 1)
print(array)