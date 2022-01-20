from pprint import pprint
def star_recursive(x, y, N, matrix):
    if N == 3:
        matrix[int(x)][int(y)] = " "
        return 1


    else:
        for i in range(int(N/3), int(N/3+N/3)):
            for j in range(int(N/3), int(N/3+N/3)):
                matrix[i+int(x)-1][j+int(y)-1] = " "
        return star_recursive(x, y, N/3, matrix) + star_recursive(x, y + N/3, N/3, matrix) + star_recursive(x, y + N/3 + N/3, N/3, matrix) + \
            star_recursive(x + N/3, y, N/3, matrix) +  star_recursive(x + N/3, y + N/3 + N/3, N/3, matrix) + \
                star_recursive(x + N/3 + N/3, y, N/3, matrix) + star_recursive(x + N/3 + N/3, y + N/3, N/3, matrix) + star_recursive(x + N/3 + N/3, y + N/3 + N/3, N/3, matrix)




N = int(input())
matrix = []
for i in range(N):
    matrix.append([])
for i in range(N):
    for j in range(N):
        matrix[i].append('*')
    

star_recursive(1, 1, N, matrix)
for i in range(0, N):
    for j in range(0, N):
        print(matrix[i][j], end ="")
    print()