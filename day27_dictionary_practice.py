#アルゴリズム
#1
matrix = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

count = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] == 1:
            count += 1

print(count)

#2
matrix = [
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 0]
]

count = 0
for i in range(3):
    for j in range(3):
        if matrix[i][j] == 1:
            count += 1

print(count)

#3
matrix = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

count = 0

i = 1
j = 1

if matrix[i-1][j] == 1: #上
    count += 1

if matrix[i+1][j] == 1: #下
    count += 1

if matrix[i][j-1] == 1: #左
    count += 1

if matrix[i][j+1] == 1: #右
    count += 1

print(count)

#4
count = 0

directions = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
]

for di, dj in directions:
    ni = i + di
    nj = j + dj

    if matrix[ni][nj] == 1:
        count += 1

#5
matrix = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(0)
    matrix.append(row)

i = 1
j = 1

matrix[i][j] = 1
matrix[i-1][j] = 1
matrix[i+1][j] = 1
matrix[i][j-1] = 1
matrix[i][j+1] = 1

for row in matrix:
    print(row)

#6
matrix = [
    [0,1,0],
    [0,0,0],
    [1,0,0]
]

i = 1
j = 1

directions = [(1,0),(-1,0),(0,1),(0,-1)]

for di, dj in directions:
    ni = i + di
    nj = j + dj

    if matrix[ni][nj] == 1:
        print("1が隣にある")

#7アルゴリズム（完成形）
count = 0

for i in range(len(matrix)):
    for j in range(len(matrix[0])):

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for di, dj in directions:

            ni = i + di
            nj = j + dj

            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
                count += 1
                break

print(count)