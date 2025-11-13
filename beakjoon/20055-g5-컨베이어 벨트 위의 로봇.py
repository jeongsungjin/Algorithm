import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(map(int, input().split())) # 내구도
robots = deque([False] * N) # 로봇 위치

step = 0

while True:
    step += 1

    belt.rotate(1)
    robots.rotate(1)
    robots[-1] = False

    for i in range(N - 2, -1, -1): # 뒤쪽부터 이동 체크
        if robots[i] and not robots[i + 1] and belt[i + 1] > 0: # 로봇 이동 가능 조건
            robots[i] = False
            robots[i + 1] = True
            belt[i + 1] -= 1

    robots[-1] = False

    if belt[0] > 0: # 새 로봇 올리기
        robots[0] = True
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(step)