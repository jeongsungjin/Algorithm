import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

air_cleaner = []

for i in range(R):
    if room[i][0] == -1:
        air_cleaner.append(i)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def spread():
    global room
    temp = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                spread_amount = room[i][j] // 5
                for dx, dy in dirs:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        temp[ni][nj] += spread_amount
                        room[i][j] -= spread_amount
    
    for i in range(R):
        for j in range(C):
            room[i][j] += temp[i][j]

    
def clean():
    top, bottom = air_cleaner

    # 위쪽 청정기(반시계)
    for i in range(top - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for i in range(C - 1):
        room[0][i] = room[0][i + 1]
    for i in range(top):
        room[i][C - 1] = room[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        room[top][i] = room[top][i - 1]
    room[top][1] = 0

    # 아래쪽 청정기 (시계)
    for i in range(bottom + 1, R - 1):
        room[i][0] = room[i + 1][0]
    for i in range(C - 1):
        room[R - 1][i] = room[R - 1][i + 1]
    for i in range(R - 1, bottom, - 1):
        room[i][C - 1] = room[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        room[bottom][i] = room[bottom][i - 1]
    room[bottom][1] = 0


for _ in range(T):
    spread()
    clean()

result = 0

for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]

print(result)