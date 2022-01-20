def number_print(M, N, arr):
    case_white = 0
    case_black = 0
    for i in range(N):
        for j in range(M):
            if (i+j) % 2 == 0:
                if arr[i][j] == 'W':
                    case_black +=1
                else:
                    case_white +=1
            else:
                if arr[i][j] == 'W':
                    case_white += 1
                else:
                    case_black +=1
    print(case_black, case_white)
    if case_black < case_white:
        return case_black
    return case_white

def number_print_new(M, N, arr):
    case_white_arr = []
    case_black_arr = []

    for i in range(N-7):
        for j in range(M-7):
            case_white = 0
            case_black = 0
            for x in range(8):
                for y in range(8):
                    if (x+y) % 2 == 0:
                        if arr[i+x][j+y] == 'W':
                            case_black +=1
                        else:
                            case_white +=1
                    else:
                        if arr[i+x][j+y] == 'W':
                            case_white += 1
                        else:
                            case_black +=1
            case_white_arr.append(case_white)
            case_black_arr.append(case_black)
    min_white = min(case_white_arr)
    min_black = min(case_black_arr)
    if min_white < min_black:
        return min_white
    return min_black


M, N = map(int, input().split())
arr = []
for i in range(M):
    row = input()
    arr.append(row)
print(number_print_new(N, M, arr))
