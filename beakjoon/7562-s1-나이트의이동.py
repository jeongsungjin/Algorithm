import sys
from collections import deque

input = sys.stdin.readline

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs(I, start, end):
    if start == end:
        return 0
    
    visited = [[False] * I for _ in range(I)]
    q = deque()

    q.append((start[0], start[1], 0)) # 시작 x, y, 이동 횟수
    visited[start[0]][start[1]] = True

    while q:
        x, y, cnt = q.popleft()
        for dx, dy in moves: # 8방향 적용
            nx, ny = x + dx, y + dy

            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]: # 새로운 방향이 방문하지 않았고, 맵 내부일때
                if (nx, ny) == end: # 목표 점이라면
                    return cnt + 1
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))


T = int(input())
for _ in range(T):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(bfs(I, start, end))
