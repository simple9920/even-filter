#書き換えを伴う処理
#1
matrix = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 1]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix != 0:#ここはmatix[i][j]  == 0:
            matrix[i][j] = 1

print(matrix)

