#1
from collections import deque

grid = [
    ['.','.','.'],
    ['.','#','.'],
    ['.','.','G']
]

H = len(grid)
W = len(grid[0])

queue = deque
queue.append((0,0,0))

visited = [[False]*W for _ in range(H)]
visited[0][0] = True

while queue:
    i, j, dist = queue.popleft()

    if grid[i][j] == 'G':
        print(dist)
        break

    for di, dj in directions:
         
         ni = i + di
         nj = j + dj

         if 0 <= ni < H and 0 <= nj < W:
             
             visited[ni][nj] = True

             queue.append((ni, nj, dist +1))

#回答
from collections import deque

grid = [
    ['.','.','.'],
    ['.','#','.'],
    ['.','.','G']
]

H = len(grid)
W = len(grid[0])

queue = deque()
queue.append((0,0,0))

visited = [[False]*W for _ in range(H)]
visited[0][0] = True

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j, dist = queue.popleft()

    if grid[i][j] == 'G':
        print(dist)
        break

    for di, dj in directions:

        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj] and grid[ni][nj] != '#':

                visited[ni][nj] = True
                queue.append((ni, nj, dist+1))

#2
from collections import deque

grid = [
    ['S','.','.','#'],
    ['.','#','.','.'],
    ['.','.','#','.'],
    ['#','.','.','G']
]

H = len(grid)
W = len(grid[0])

for i in range(H):
    for j in range(W):

        if grid[i][j] == 'S':
            si = i
            sj = j

queue = deque()
queue.append((si, sj, 0))

visted = [[False]*W for _ in range(H)]
visted[si][sj] = True

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j, dist = queue.popleft()

    if grid[i][j] == 'G':
        print(dist)
        break

    for di, dj in directions:

        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj] and grid[ni][nj] != '#':

                visited[ni][nj] = True
                queue.append((ni, nj dist+1))

#回答
from collections import deque

grid = [
    ['S','.','.','#'],
    ['.','#','.','.'],
    ['.','.','#','.'],
    ['#','.','.','G']
]

H = len(grid)
W = len(grid[0])

for i in range(H):
    for j in range(W):

        if grid[i][j] == 'S':
            si = i
            sj = j

queue = deque()
queue.append((si, sj, 0))

visited = [[False]*W for _ in range(H)]
visited[si][sj] = True

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:

    i, j, dist = queue.popleft()

    if grid[i][j] =='G':
        print(dist)
        break

    for di, dj in directions:

        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj] and grid[ni][nj] != '#':

                visited[ni][nj] = True
                queue.append((ni, nj, dist+1))

