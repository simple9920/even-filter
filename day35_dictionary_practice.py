#復習
from collections import deque

H = len(grid)
W = len(grid[0])

visited = [[False]*W for _ in range(H)]

directions = [(1,0),(-1,0),(0,1),(0,-1)]

count = 0

for i in range(H):
    for j in range(W):


        if grid[i][j] == 1 and not visited[i][j]:

            count += 1

            queue = deque()
            queue.append((i,j))
            visited[i][j] = True

            while queue:

                ci, cj = queue.popleft()

                for di,dj in directions:
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < H and 0 <= nj < W:

                        if grid[ni][nj] == 1 and not visited[ni][nj]:

                            visited[ni][nj] = True
                            queue.append((ni,nj))

# Multi-soure\ce BFS テンプレ
queue = deque()

#⓵  スタート地点を全部入れる
for i in range(H):
    for j in range(W):
        if grud[i][j] == 1:
            queue.append((i,j))

#⓶BFS
while queue:
    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:
            if 条件:
                queue.append((ni,nj))

#BFS最短距離テンプレ
from collections import deque

queue = deque()
queue.append((si,sj))

dist  [[-1]*W for _ in range(H)] #dist== -1なら未訪問 >=0なら訪問済み
dist[si][sj] = 0

while queue:

    i, j = queue.popleft()

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W:

            if dist[ni][nj] == -1:

                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni,nj))