import sys
max_res = -1000000001
min_res = 1000000001
def op_p(arr, depth, M, res, A):
    global max_res
    global min_res
    op = ['+', '-', '*', '/']
    if depth == M:
        # print(res, end = " ")
        str_eval = ""
        for i in range(M+1):
            str_eval += str(A[i])
            str_eval = str(int(eval(str_eval)))
            if i == M:
                continue
            str_eval += res[i]
        #print(eval(str_eval))
        if max_res < eval(str_eval):
            max_res = eval(str_eval)
        if min_res > eval(str_eval):
            min_res = eval(str_eval)
    else:
        # 순회하기
        for i in range(4):
            if arr[i] != 0:
                res[depth] = op[i]
                arr[i] -= 1
                op_p(arr, depth+1, M, res, A)
                arr[i] += 1




N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
O = list(map(int, sys.stdin.readline().split()))

res = [0] * (N-1)
arr = O


#print(arr)
op_p(arr, 0, N-1, res, A)
print(max_res)
print(min_res)

# arr[0] = '+'
# arr[1] = '-`
# arr[2] = '*'
# arr[3] = '/'