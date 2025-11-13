import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * M for _ in range(N)]
answer = 0

def dfs(x, y, depth, total):
    global answer

    if depth == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited[nx][ny] = False

def check_extra_shape(x, y): # ㅜㅗㅓㅏ 모양
    global answer

    for exclude in range(4):
        temp = board[x][y] # 중심점 값
        vaild = True
        for i in range(4): # 뻗어 나갈 상하좌우 4방향
            if i == exclude:  # 제외할 방향
                continue

            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                vaild = False
                break
            temp += board[nx][ny]
        if vaild:
            answer = max(answer, temp)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_extra_shape(i, j)

print(answer)