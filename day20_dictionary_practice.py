matrix = []

for i in range(3):
    matrix.append([0, 0, 0])

for i in range(3):
    for j in range(3):
        if i + j == 2:
            matrix[i][j] = 1

print(matrix)