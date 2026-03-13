#BFSテンプレ
from collections import deque

grid = [
    ['S','.','.'],
    ['.','#','.'],
    ['.','.','G']
]

H = 3
W = 3

si, sj = 0, 0

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

            if grid[ni][nj] != '#' and not visited[ni][nj]: #grid[ni][nj] != '#' 意味:壁は進めない

                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))

#暗記
from collections import deque

queue = deque() #queueを作る
queue.append((si, sj)) #startに入れる

visited[si][sj] = True 

while queue:
    i, j = queue.popleft() #一番左を取り出す

    for di, dj in directions: #4方向
        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W: #境界
            if grid[ni][nj] != '#' and not visited[ni][nj]: #壁

                visited[ni][nj] = True
                dist[ni][nj] = dist[i][j] + 1 #dist更新
                queue.append((ni, sj))