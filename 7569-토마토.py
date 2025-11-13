from collections import deque
import sys
input = sys.stdin.read

def bfs():
    directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    while queue:
        z, x, y = queue.popleft()
        for dz, dx, dy in directions:
            nz, nx, ny = z + dz, x + dx, y + dy
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                queue.append((nz, nx, ny))


data = input().strip().splitlines()
M, N, H = map(int, data[0].split())
box = []
queue = deque()


for h in range(H):
    floor = []
    for n in range(N):
        row = list(map(int, data[1 + h * N + n].split()))
        for m in range(M):
            if row[m] == 1:
                queue.append((h, n, m))
        floor.append(row)
    box.append(floor)

bfs()

max_days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                sys.exit(0)
            max_days = max(max_days, box[h][n][m])

print(max_days - 1)