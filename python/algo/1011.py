def min_number(a, b):
    arr = []
    for i in range(a, b+1):
        arr.append(i)
    
    left = 0                #왼쪽 시작점
    right = len(arr) - 1    #오른쪽 시작점
    left_distance = 1       #왼쪽 이동 거리 증가폭
    right_distance = 1      #오른쪽 이동 거리 증가폭
    count = 0               #이동횟수
    while True:
        if left >= right:   #왼쪽 인덱스가 오른쪽 인덱스를 만나거나 초과하면 break
            break
        left += left_distance
        count +=1           #왼쪽 인덱스에서 이동1번

        if left >= right:
            break           #오른쪽인덱스 도달시 break
        right -= right_distance
        count +=1           #오른쪽인덱스에서 이동1번

        if left >= right:
            break           #도달시 break  

        left_distance += 1  #기본적으로 1씩 증가
        right_distance += 1 #기본적으로 1씩 증가
    return count
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(min_number(a, b))