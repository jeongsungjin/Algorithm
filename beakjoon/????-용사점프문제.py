from collections import deque

# 예제 입력
N = 5
grid = [
    [0,0,0,1,0],
    [0,1,0,2,0],
    [0,0,0,0,0],
    [2,0,1,0,0],
    [0,0,0,0,0]
]
sx, sy = 0, 0
gx, gy = 4, 4

# 방향: 상(0), 하(1), 좌(2), 우(3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 한 칸 점프 후 위치 계산
def get_next_pos(x, y, dir, jump):
    nx = x + dx[dir] * jump
    ny = y + dy[dir] * jump
    return nx, ny

# 격자 이동 가능 여부
def can_move(nx, ny):
    return 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 1

def bfs():
    queue = deque()
    # 시작 상태: (x, y, 방향, 점프 거리, 턴 수)
    queue.append((sx, sy, 0, 1, 0))
    
    # 방문 체크: (x, y, 방향, 점프 거리)
    visited = dict()
    visited[(sx, sy, 0, 1)] = True

    while queue:
        x, y, dir, jump, turns = queue.popleft()
        
        # 목표 도달
        if x == gx and y == gy:
            return turns

        # ----- 한 턴에서 3가지 액션 -----

        # 1) 점프 이동
        nx, ny = get_next_pos(x, y, dir, jump)
        # 이동 가능하고 아직 방문하지 않은 상태면 큐에 추가
        if can_move(nx, ny) and (nx, ny, dir, jump) not in visited:
            visited[(nx, ny, dir, jump)] = True
            queue.append((nx, ny, dir, jump, turns+1))

        # 2) 방향 전환
        for ndir in range(4):
            if ndir != dir and (x, y, ndir, jump) not in visited:
                visited[(x, y, ndir, jump)] = True
                queue.append((x, y, ndir, jump, turns+1))

        # 3) 점프 충전
        if (x, y, dir, jump+1) not in visited:
            visited[(x, y, dir, jump+1)] = True
            queue.append((x, y, dir, jump+1, turns+1))
        # --------------------------------

    # 도달 불가
    return -1

result = bfs()
print(result)
