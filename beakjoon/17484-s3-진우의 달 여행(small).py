import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1]

answer = 10**9

def dfs(r, c, prev_dir, fuel):
    global answer

    if r == N - 1: # 마지막 행 도달, 최소값 갱신
        answer = min(answer, fuel)
        return
    
    for dir in range(3):
        if dir == prev_dir:
            continue

        nr = r + 1
        nc = c + dr[dir]

        if 0 <= nc < M:
            dfs(nr, nc, dir, fuel + matrix[nr][nc])

# 모든 열 선택 가능

for start_col in range(M):
    dfs(0, start_col, -1, matrix[0][start_col])

print(answer)