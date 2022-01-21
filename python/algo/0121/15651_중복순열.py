def dfs_overlap(depth, N, M, res):
    if depth == M:
        for i in res:
            print(i, end =" ")
        print()
    else:
        for i in range(1, N+1):
            res[depth] = i
            dfs_overlap(depth+1, N, M, res)



N = 5
M = 2
res = [0] * M
dfs_overlap(0, N, M, res)