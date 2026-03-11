#復習1
from collections import deque

queue = deque()
queue.append((si, sj))

visited[si][sj] = True

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if not visited[ni][nj]:

                visited[ni][nj] = True
                queue.append((ni, nj))

#復習2
from collections import deque

grid = [
    ['S','.','.','#'],
    ['.','#','.','.'],
    ['.','.','#','.'],
    ['#','.','.','G']
]

H = 4
W = 4

queue = deque
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

#3
from collections import deque

grid = [
['S','.','.','#','.','.'],
['.','#','.','#','.','.'],
['.','#','.','.','.','#'],
['.','.','#','#','.','.'],
['#','.','.','.','#','.'],
['.','.','#','.','.','G']
]

H = 6
W = 6

queue = deque()
queue.append((0,0))

dist = [[-1]*W for _ in range(H)]
dist[0][0] = 0

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:

    i, j = queue.popleft()

    for di, dj in directions:

        if 0 <= ni < H and 0 <= nj < W:

            if dist[ni][nj] == -1 and grid[ni][nj] != '#':

                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))

#4
from collections import deque

grid = [
[2,1,1],
[1,1,0],
[0,1,1]
]

H = 3
W = 3

queue = deque()

for i in range(H):
    for j in range(W):
        if grid[i][j] == 2: 
            queue.append((i,j))

directions = [(1,0),(-1,0),(0,1),(0,-1)]

time = 0

while queue:

    size = len(queue) #処理するキューの数　

    for _ in range(size):

        i, j = queue.popleft()

        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if grid[ni][nj] == 1:

                grid[ni][nj] = 2
                queue.append((ni, nj))

    time += 1

#5
grid = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]
]

H = 4
W = 5

visited = [[False]*W for_ in range(H)]

def dfs(i,f):

    if i < 0 or i >= H or j < 0 or j >= W:
        return 0
    
    if grid[i][j] == 0 or visited[i][j]:
        return 0
    
    visited[i][j] = True

    size = 1 #今のマス

    size += dfs(i+1,j) #つながっているマスを全部足す DFSでサイズ計算
    size += dfs(i-1,j)
    size += dfs(i,j+1)
    size += dfs(i,j-1)

    return size


max_island = 0

for i in range(H): #グリッド全探索
    for j in range(W):

        if grid[i][j] == 1 and not visited[i][j]:

            island_size = dfs(i,j)
            max_island = max(max_island, island_size) #最大値更新

print(max_island)