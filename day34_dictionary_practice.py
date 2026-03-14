#島カウントBFSの基礎構造
count = 0

for i in range(H):
    for j in range(W):

        if grid[i][j] == 1 and not visited[i][j]:

            count += 1
            queue.append((i,j))
            visited[i][j] = True

            while queue:
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < H and 0 <= ny < W:
                        if grid[nx][ny] == 1 and not visited[nx][ny]: #0に進むのを防ぐ「陸のマスのだけ探索する」
                            visited[nx][ny] = True
                            queue.append((nx,ny))