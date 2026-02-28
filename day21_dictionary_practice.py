#[[0]*3]*3 危険性
matrix = [[0]*3]*3
matrix[0][0] = 1

print(matrix)

#安全な書き方
matrix = []
for i in range(3):
    matrix.append8([0]*3)

#or

matrix = [[0]*3 for _ in range(3)]

#

a = [[1, 2], [3, 4]]

b = []

for row in a:
    b.append(row.copy()) #内部リストを新しく作る or b = [row.copy() for row in a]

b[0][0] = 9

print(a)#別構造
print(b)#別構造