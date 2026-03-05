#応用2Dリスト
#1
matrix = []

for i in range(3):
    row = [0]*3
    matrix.append(row)

print(matrix)

#2
matrix = []

for i in range(3):
    row = []

    for j in range(3):
        if i == j:
            row.append(1)
        else:
            row.append(0)

    matrix.append(row)

print(matrix)

#3
matrix = []

for i in range(3):
    row = []

    for j in range(3):
        if i + j == 2:
            row.append(1)
        else:
            row.append(0)


    matrix.append(row)

print(matrix)

#4
matrix = []

for i in range(3):
    row = []

    for j in range(3):
        if not(i == 1 and j == 1):
            row.append(1)
        else:
            row.append(0)

    matrix.append(row)
print(matrix)

#5
matrix = []

for i in range(3):
    row = []

    for j in range(3):
        if i == j:
            row.append(0)
        else:
            row.append(1)

    matrix.append(row)
print(matrix)