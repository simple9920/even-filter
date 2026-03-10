#
grid = [
    [1,1,0],
    [1,0,0],
    [0,0,1]
]

H = len(grid)
W = len(grid[0])

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(i,j):

    grid[i][j] = 0

    for di,dj in directions:

        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if grid[ni][nj] == 1:
                dfs(ni,nj)

count = 0

for i in range(H):
    for j in range(W):

        if grid[i][j] == 1:

           count += 1
           dfs(i,j)

print(count) 