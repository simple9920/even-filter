#1
def dfs(i, j):

    grid[i][j] = 0 #訪問済み

    for di, dj in directions: #周囲探索

        ni = i + di
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W: #範囲チェック

            if grid[ni][nj] == 1: #未訪問なら次へ進む
                dfs(ni, nj)

            
#2島の数
count = 0

for i in range(H):
    for j in range(W):

        if grid[i][j] == 1:
            count += 1
            dfs(i, j)

#3 bfs基本テンプレ
from collections import deque

queue = deque()
queue.append((start_r, sttart_c))

while queue:
    r, c = queue.popleft()

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

#3
from collections import deque
grid = [
    ['S','0','0'],
    ['1','1','0'],
    ['0','0','G']
]

rows = len(grid) #行数
cols = len(grid[0]) #列数

directions = [(1,0),(-1,0),(0,1),(0,-1)] #移動方向上下左右

queue = deque([(0,0,0)]) #r,c,dist　位置(0,0)距離0
visited = set([(0,0)]) #すでに訪れた場所

while queue: #キューが空になるまで探索
    r,c,d = queue.popleft() #キューから取り出す

    if grid[r][c] == 'G': #ゴールチェック
        print(d) #最初にゴールした距離
        break

    for dr,dc in directions: #方向リスト上下左右を使う
        nr = r+dr
        nc = c+dc

        if 0<=nr<rows and 0<=nc<cols: #グリッド外にでないようにする
            if (nr,nc) not in visited and grid[nr][nc] != '1': #まだ行ってない、壁じゃない
                visited.add((nr,nc)) #訪れた記録
                queue.append((nr,nc,d+1)) #次の探検候補に追加d+1は距離