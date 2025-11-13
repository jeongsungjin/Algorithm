import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())
apple_points = [tuple(map(int, input().split())) for _ in range(K)] # 좌표를 리스트에 튜플 자료형으로 넣기

L = int(input().strip())
dir_points = [list(input().split()) for _ in range(L)]
dir_points = [(int(x), c) for x, c in dir_points] # 리스트의 각 인자에 대해서 int, 문자열 처리

# 우, 하, 좌, 상 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate():
    board = [[0] * (N + 1) for _ in range(N + 1)] # NxN 보드 0으로 초기화. 뱀의 초기 위치가 (1,1)이래서 (N + 1) 처리

    for x, y in apple_points:
        board[x][y] = 1

    snake = deque([(1 , 1)]) # 뱀의 초기위치 (1,1), 뱀의 머리와 꼬리만 처리하면 되니 deque 사용
    direction = 0
    time = 0
    idx = 0 # 회전 시점 관리 변수

    while True:
        time += 1
        head_x, head_y = snake[-1] # 맨 오른쪽이 머리
        nx, ny = head_x + dx[direction], head_y + dy[direction] # 진행 방향으로 머리 진행
        
        if not (1 <= nx <= N) or not(1 <= ny <= N): # 맵 범위 내에 nx, ny 둘중에 하나라도 포함되지 않는다면,
            return time
        if (nx, ny) in snake:
            return time
        
        if board[nx][ny] == 1:
            board[nx][ny] = 0
            snake.append((nx, ny))
        else:
            snake.append((nx, ny))
            snake.popleft() # 사과 못먹었으니 꼬리 줄이기

        if idx < L and time == dir_points[idx][0]: #  idx로 회전 시점 관리, 현재 시간이 회전 시간일때
            if dir_points[idx][1] == 'L': # 왼쪽으로 90도
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            idx += 1
            

print(simulate())