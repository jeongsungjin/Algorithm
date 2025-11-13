import sys

input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [0, 1, 2 ,3] # 상하좌우

max_block = 0

def move(board, direction):
    new_board = [[0] * N for _ in range(N)]

    if direction == 0: # 상
        for c in range(N):
            idx = 0 # 위쪽으로 채워넣을 인덱스(행)
            prev = 0
            for r in range(N):
                if board[r][c] != 0:
                    if prev == 0: # 합칠 블록 없음
                        prev = board[r][c]
                    elif prev == board[r][c]:
                        new_board[idx][c] = prev * 2 # 합쳐짐
                        prev = 0 # 합쳣으니 후보 초기회
                        idx += 1
                    else: # 안 합쳐짐, Prev 확정
                        new_board[idx][c] = prev
                        prev = board[r][c]
                        idx += 1
            if prev != 0:
                new_board[idx][c] = prev

    elif direction == 1: # 하
        for c in range(N):
            idx = N - 1 # 아래쪽으로 채울 인덱스 (행)
            prev = 0
            for r in range(N - 1, -1, -1):
                if board[r][c] != 0:
                    if prev == 0:
                        prev = board[r][c]
                    elif prev == board[r][c]:
                        new_board[idx][c] = prev * 2
                        prev = 0
                        idx -= 1
                    else:
                        new_board[idx][c] = prev
                        prev = board[r][c]
                        idx -= 1
            if prev != 0:
                new_board[idx][c] = prev
    
    elif direction == 2: # 좌
        for r in range(N):
            idx = 0 # 왼쪽으로 채울 인덱스 0부터 증가
            prev = 0
            for c in range(N):
                if board[r][c] != 0:
                    if prev == 0:
                        prev = board[r][c]
                    elif prev == board[r][c]:
                        new_board[r][idx] = prev * 2
                        prev = 0 # 합쳣으니 초기화
                        idx += 1
                    else:
                        new_board[r][idx] = prev
                        prev = board[r][c]
                        idx += 1
            if prev != 0:
                new_board[r][idx] = prev
    
    elif direction == 3: # 우
        for r in range(N):
            idx = N - 1 # 오른쪽으로 채울 인덱스  N -1 부터 감소
            prev = 0
            for c in range(N - 1, -1, -1):
                if board[r][c] != 0:
                    if prev == 0:
                        prev = board[r][c]
                    elif prev == board[r][c]:
                        new_board[r][idx] = prev * 2
                        prev = 0 # 합쳤으니 후보 초기화
                        idx -= 1
                    else:
                        new_board[r][idx] = prev
                        prev = board[r][c]
                        idx -= 1
            if prev != 0:
                new_board[r][idx] = prev
    
    return new_board

def dfs(board, depth):
    global max_block

    if depth == 5:
        for r in range(N):
            max_block = max(max_block, max(board[r]))
        return
    
    for d in dirs:
        new_board = move(board, d)
        dfs(new_board, depth + 1)


dfs(board, 0)
print(max_block)