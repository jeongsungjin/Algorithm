import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def bfs():

    queue = deque()
    queue.append((0, 0, 0, 1)) # 시작점, 벽 파괴 안함, 이동 거리 1

    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True

    while queue:
        x, y, wall_brake, dist = queue.popleft()

        if x == N - 1 and y == M - 1:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if board[nx][ny] == 0 and not visited[nx][ny][wall_brake]:
                    visited[nx][ny][wall_brake] = True
                    queue.append((nx, ny, wall_brake, dist + 1))
                elif board[nx][ny] == 1 and wall_brake == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

        
        return -1

print(bfs())
