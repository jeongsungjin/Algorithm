import sys

input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

count = 0
# 방향 => 0: 가로, 1: 세로, 2: 대각선
def dfs(x, y, direction):
    global count

    if x == N - 1 and y == N - 1:
        count += 1
        return
    
    # 가로 방향
    if direction == 0:
        # 오른쪽 가능?
        if (0 <= y + 1 < N) and (board[x][y + 1] == 0):
            dfs(x, y + 1, 0)
        # 대각선 가능?
        if (0 <= x + 1 < N) and (0 <= y + 1 < N) and (board[x][y + 1] == 0) and (board[x + 1][y] == 0) and (board[x + 1][y + 1] == 0):
            dfs(x + 1, y + 1, 2)

    if direction == 1:
        # 아래로 가능?
        if (0 <= x + 1 < N) and (board[x + 1][y] == 0):
            dfs(x + 1, y, 1)
        # 대각선 가능?
        if (0 <= x + 1 < N) and (0 <= y + 1 < N) and (board[x][y + 1] == 0) and (board[x + 1][y] == 0) and (board[x + 1][y + 1] == 0):
            dfs(x + 1, y + 1, 2)

    if direction == 2:
        # 오른쪽 가능?
        if (0 <= y + 1 < N) and (board[x][y + 1] == 0):
            dfs(x, y + 1, 0)
        # 아래로 가능?
        if (0 <= x + 1 < N) and (board[x + 1][y] == 0):
            dfs(x + 1, y, 1)
        # 대각선 가능?
        if (0 <= x + 1 < N) and (0 <= y + 1 < N) and (board[x][y + 1] == 0) and (board[x + 1][y] == 0) and (board[x + 1][y + 1] == 0):
            dfs(x + 1, y + 1, 2)

dfs(0, 1, 0)

print(count)