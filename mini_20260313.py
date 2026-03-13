#1
from collections import deque
grid = [
    ['S','.','.'],
    ['#','#','.'],
    ['.','.','G']
]

H = 3
W = 3

queue = deque()
queue.append((0,0))

visited = [[False]*W for _ in range(H)]
visited.append()

dist = 

#1　回答
from collections import deque

grid = [
    ['S','.','.'],
    ['#','#','.'],
    ['.','.','G']
]

H = 3
W = 3

queue = deque()
queue.append((0,0))

visited = [[False]*W for _ in range(H)]
visited[0][0] = True

dist = [[0]*W for _ in range(H)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

#2
while queue:
    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj]:
                visited[ni][nj] = True

                dist.
                queue.append((ni, nj, dist+1))

#2回答
while queue:
    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj]:
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))

#3
from collections import deque

grid = [
    ['S','.','.']
    ['#','#','.']
    ['.','.','G']
]

H = 3
W = 3

queue = deque()
queue.append((0,0))

visited = [[False]*W for _ in range(H)]
visited[0][0] = True

dist = [[0]*W for _ in range(H)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i , j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if grid[i][j] != '#' and not visited[ni][nj]:

                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni,nj))
    
#3回答
grid = [
    ['S','.','.'],
    ['#','#','.'],
    ['.','.','G']
]

if grid[ni][nj] != '#' and not visited[ni][nj]: #次に行く場所