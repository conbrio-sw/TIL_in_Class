def dfs(depth, N, M, res):
    if depth == M:
        for i in range(0, M-1):
            if res[i] > res[i+1]:
                return
        for i in res:
            print(i, end=' ')
        print()
    else:
        for i in range(1, N+1):
            if ch[i] == 0:
                ch[i] = 1
                
                res[depth] = i
                # if depth != 0:
                #     if res[depth-1] > res[depth]:
                #         print(res[depth-1], res[depth], "====================")
                #         return
    
                dfs(depth+1, N, M, res)
                ch[i] = 0

N = 5
M = 2

res = [0] * M
ch = [0] * (N+1)
dfs(0, N, M, res)


N, M = map(int, input().split())

res = [0] * M

ch = [0] * (N+1)

dfs(0, N, M, res)
