n = 7 

matrix = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(n):
        if i + j < n:
            matrix[i][j] = i + j + 1


for row in matrix:
    print(row)
