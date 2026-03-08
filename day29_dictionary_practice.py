#1
from collections import deque
grid = [
    [1,1,0,0],
    [1,0,0,1],
    [0,0,1,1],
    [0,0,0,0]
]

H = len(grid)
W = len(grid[0])

visited = [[False]*W for _ in range(H)]

directions = [(-1,0),(1,0),(0,-1),(0,1)]

count = 0

for i in range(H):
    for j in range(W): #全マス見る

        if grid[i][j] == 1 and not visited[i][j]: #新しい島を見つける

            count += 1 #新しい島を発見
            q = deque() #BFS開始
            q.append((i,j))
            visited[i][j] = True # キュー
            
            while q: #キューが空になるまで探索
                x,y = q.popleft() # 1個取り出す

                for dx,dy in directions: # 上下左右を見る
                    nx = x + dx #新しい座標を作る
                    ny = y + dy

                    if 0 <= nx < H and 0 <= ny < W: #境界チェック
                        if grid[nx][ny] == 1 and not visited[nx][ny]: #次の陸を見つける　まだ探索していないなら同じ島
                            visited[nx][ny] = True #キューの追加　探索済み
                            q.append((nx,ny))

print(count)

#2DFS 島探索
def dfs(i, j): #(i,j)から島を探索する

    visited[i][j] = True # 訪問記録ここは探索済み
    for dx, dy in directions: # 上下左右　4方向チェック

        ni = i + dx #隣の座標
        nj = j + dy

        if 0 <= ni < H and 0 <= nj < W: # 境界チェック

            if grid[ni][nj] == 1 and not visited[ni][nj]: # 次の島を発見、まだ探索していない陸
                dfs(ni, nj) # 再帰 さらに探索

#3島全体の全体コード
count = 0

for i in range(H):
    for j in range(W):

        if grid[i][j] == 1 and not visited[i][j]:
            count += 1
            dfs(i, j)

#4DFSサイズ
def dfs(i, j):

    visited[i][j] = True
    size = 1

    for dx, dy in directions:

        ni = i + dx
        nj = j + dy

        if 0 <= ni < H and 0 <= nj < W:

            if grid[ni][nj] == 1 and not visited[ni][nj]:
                size += dfs(ni, nj) #　自分+隣のサイズ

    return size

#5最大サイズ
max_size = 0

for i in range(H):
    for j in range(W):

        if grid[i][j] == 1 and not visited[i][j]:

            size = dfs(i, j)
            max_size = max(max_size, size)