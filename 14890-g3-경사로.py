import sys

input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input(). split())) for _ in range(N)]

def check(line):

    used = [False] * N

    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue

        if abs(line[i] - line[i + 1]) > 1:
            return False
        
        if line[i] < line[i + 1]: # 오르막, 진행 방향이 더 높은 경우
            h = line[i] # 오르막 기준 높이. 낮은 곳
            for j in range(i, i - L, -1): # 뒤로 L칸 검사(경사로 설치를 위한)
                if j < 0 or line[j] != h or used[j]: # 경사로 설치 못함
                    return False
                used[j] = True

        else: # 내리막, 진행 방향이 더 낮은 경우
            h = line[i + 1] # 낮은 곳. 경사 기준 높이
            for j in range(i + 1, i + L + 1):
                if N <= j or line[j] != h or used[j]:
                    return False
                used[j] = True

    return True

ans = 0

for r in range(N):
    if check(board[r]):
        ans += 1

for c in range(N):
    col = [board[r][c] for r in range(N)] # 열 검사, 세로줄 추출
    if check(col):
        ans += 1

print(ans)
