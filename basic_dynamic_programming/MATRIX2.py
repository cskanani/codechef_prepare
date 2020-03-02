from sys import stdin
rows, columns = map(int, stdin.readline().split())
matrix = []
for i in range(rows):
    matrix.append(list(map(int, list(stdin.readline().strip()))))

for j in range(1, columns):
    for i in range(rows-2, -1, -1):
        if matrix[i][j]:
            matrix[i][j] = min(matrix[i+1][j]+1, matrix[i][j-1]+1)
                
#for row in matrix:
    #print(' '.join(map(str, row)))

possible_sub_matrix = 0
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] != 0:
            possible_sub_matrix += matrix[i][j]
print(possible_sub_matrix)
