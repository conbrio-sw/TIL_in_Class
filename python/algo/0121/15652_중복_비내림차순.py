def dfs_overlap(depth, N, M, res):
    if depth == M:
        # for i in range(M-1):
        #     if res[i] > res[i+1]:
        #         return
        for i in res:
            print(i, end =" ")
        print()
    else:
        for i in range(1, N+1):
            if depth != 0:
                if i < res[depth-1]:
                    continue




            res[depth] = i
            dfs_overlap(depth+1, N, M, res)


N, M = map(int, input().split())

res = [0] * M

ch = [0] * (N+1)

dfs_overlap(0, N, M, res)
