import sys
from collections import deque
input = sys.stdin.readline

# 8방향(좌상, 상, 우상, 우, 우하, 하, 좌하, 좌)
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0

    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                count += 1

    print(count)



# dfs로 푸니까 메모리 초과남

# def dfs(x, y):
#     visited[y][x] = True
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < w and 0 <= ny < h:
#             if not visited[ny][nx] and graph[ny][nx] == 1:
#                 dfs(nx, ny)


# while True:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break

#     graph = [list(map(int, input().split())) for _ in range(h)]
#     visited = [[False] * w for _ in range(h)]

#     count = 0

#     for y in range(h):
#         for x in range(w):
#             if graph[y][x] == 1 and not visited[y][x]:
#                 dfs(x, y)
#                 count += 1
    
#     print(count)




    