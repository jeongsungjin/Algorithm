import sys

input = sys.stdin.readline

N = int(input().strip())
students = [list(map(int, input().split())) for _ in range(N * N)]
# 각 행의 첫번째 열은 학생 번호, 뒷 4개는 좋아하는 학생 번호

board = [[0] * (N + 1) for _ in range(N + 1)] # 자리 초기화

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

like_dict = dict()
for s in students:
    like_dict[s[0]] = s[1:] # 각 학생이 좋아하는 학생 4명 딕셔너리로 저장

def seat_student(seat_id):
    max_like = -1 # 좋아하는 학생 최대 인접 수
    max_empty = -1 # 인접한 빈 칸 수의 최대값
    candidate = [] # 후보 위치

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] != 0:
                continue
            
            like_cnt = 0 # 인접 좋아하는 학생 수
            empty_cnt = 0 # 인접 빈칸 수

            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if (1 <= nx <= N) and (1 <= ny <= N): # 교실 범위 내
                    if board[nx][ny] in like_dict[seat_id]:
                        like_cnt += 1 # 새 좌표에 좋아하는 학생이 잇다면
                    elif board[nx][ny] == 0:
                        empty_cnt += 1 # 없다면
            
            if like_cnt > max_like or (like_cnt == max_like and empty_cnt > max_empty):
                # 좋아하는 학생이 가장 많은 칸 (1), (1)이 만족한다면 인접한 칸 중 가장 비어있는 칸이 많은 칸
                candidate = [(i, j)] # 현재 학생이 앉을 수 있는 후보 위치, 계속 해서 더 좋은 좌표가 나오면 새로운 좌표 삽입
                max_like = like_cnt
                max_empty = empty_cnt
            elif like_cnt == max_like and empty_cnt == max_empty:
                candidate.append((i, j))
            
    # 행 -> 열 작은순으로 sort
    candidate.sort()
    r, c = candidate[0]
    board[r][c] = seat_id # 계산된 좌표에 seat_id 배치

for s in students:
    seat_student(s[0])

score = 0
score_map = [0, 1, 10, 100, 1000]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        seat_id = board[i][j]
        like_cnt = 0

        for d in range(4):
            nx, ny = i + dx[d], j + dy[d]
            if (1 <= nx <= N) and (1 <= ny <= N):
                if board[nx][ny] in like_dict[seat_id]: # 인접 좌표에 좋아하는 학생이 있다면!
                    like_cnt += 1
        
        score += score_map[like_cnt]

print(score)
    

                

