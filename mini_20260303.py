#1
a = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            a[i][j] = 9

print(a)

#2
a = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        if i != 1 or j != 1: #not(i == 1 and j == 1)
            a[i][j] = 9

print(a)