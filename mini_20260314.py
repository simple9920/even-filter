#BFSテンプレ見ずに
from collections import deque

queue = deque()
queue.append((si, sj))

visited = [[False]*W for _ in range(H)]
visited[si][sj] = True

dist = [[0]*W for _ in range(H)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j = queue.popleft()

    for di, dj in range(H): # for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj]:
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] # dist[ni][nj] = dist[i][j] +1
                queue.append((ni, nj))

#もう一度
from collections import deque

queue = deque()
queue.append((si, sj))

visited = [[False]*W for _ in range(H)]
visited[si][sj] = True

dist = [[0]*W for _ in range(H)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if not visited[ni][nj]:
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] +1
                queue.append((ni, nj))

#1
from collections import deque
H = 3
W = 4

grid = [
    "s..#",
    ".#..",
    "...G"
]

visited =[[False]*W for _ in range(H)]
visited[0][0] = True

dist = [[0]*W for _ in range(H)]

queue = deque()
queue.append((0,0))

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if grid[ni][nj] != '#' and not visited[ni][nj]:
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] +1
                queue.append((ni, nj))

#1解
from collections import deque

H = 3
W = 4

grid = [
    "S..#",
    ".#..",
    "...G"
]

visited = [[False]*W for _ in range(H)]
dist = [[0]*W for _ in range(H)]

queue = deque()

#Sを探す
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            si, sj = i, j

queue.append((si, sj))
visited[si][sj] = True

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j = queue.popleft()

    if grid[i][j] == 'G':
        print(dist[i][j])
        break

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if grid[ni][nj] != '#' and not visited[ni][nj]:
                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] +1
                queue.append((ni, nj))