import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[0] * M  for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    dist[x][y] = 1 # 시작점 거리

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): # 맵 밖 조건
                continue

            if graph[nx][ny] == 0 or dist[nx][ny] != 0: # 벽이거나, 방문 한 곳일때
                continue

            dist[nx][ny] = dist[cx][cy] + 1
            q.append((nx, ny))


    return dist[N - 1][M - 1]

print(bfs(0, 0))