#1BFSコードテンプレ
from collections import deque

queue = deque()
queue.append((si, sj, 0)) #座標 + 距離

visited = set() #同じ場所を2回探索しない
visited.append((si, sj))

while queue:
    i, j, dist = queue.popleft() #今いるマス、スタートからの距離

    if (i, j) == goal:
        print(dist)

    for di, dj in directions: #上下左右をみる
        ni = i + di #次の場所を作る
        nj = j + dj

        if 0 <= ni < H and 0 <= nj < W: #行けるかチェック
            if grid[ni][nj] != '#' and (ni, nj) not in visited: # 壁なら進めない、まだ訪れていないマス
                visited.add((ni, nj)) #訪れた印をつける
                queue.append((ni, nj, dist + 1)) #1歩進む、次をキューへ

#2
from collections import deque

grid = [
    ["S",".",".","."],
    ["#","#",".","#"],
    [".",".",".","#"],
    [".","#","G","."]
]

H = 4
W = 4

queue = deque()
queue.append((0,0,0))

visited = set()
visited.add((0,0))

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    i, j, dist = queue.popleft()

    if grid[i][j] == "G":
        print(dist)

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni <H and 0 <= nj < W:
            if grid[ni][nj] != "#" and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj, dist + 1))