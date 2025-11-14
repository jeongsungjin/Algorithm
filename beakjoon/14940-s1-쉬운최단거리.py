import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

start_x = start_y = 0

# bfs

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i, j
            dist[i][j] = 0

q = deque()
q.append((start_x, start_y))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                continue

            if dist[nx][ny] == -1: # 아직 방문하지 않은 땅
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dist[i][j] = 0


for row in dist:
    print(*row)