import sys
from collections import deque

input = sys.stdin.readline

gears = [deque(map(int, list(input().strip()))) for _ in range(4)]
#4개의 deque로 gear를 저장. 

K = int(input().strip())

for _ in range(K):
    num, direction = map(int, input().split()) # 기어 번호, 방향
    idx = num - 1

    rotations = [0] * 4 #4개에 기어에 대해서 회전 방향을 저장할 배열
    rotations[idx] = direction

    # 왼쪽으로 propagation
    # idx에서 왼쪽으로 갈수록 i - 1과 i 비교
    # 비교 방법 -> 왼쪽 기어의 오른쪽 톱니(인덱스 2), 현재 기어의 왼쪽 톱니(인덱스 6)
    for i in range(idx, 0, - 1): # 현재 기어 번째부터 0번째 기어까지 내려가면서
        if gears[i - 1][2] != gears[i][6]: #극성이 다르다면        
            rotations[i - 1] = -rotations[i] # 현재 기어가 돌았으니, 인접 기어는 반대 방향으로 회전
        else:
            break
    
    # 오른쪽으로 propagation
    # idx에서 오른쪽으로 갈수록 i와 i + 1 비교
    # 비교 방법 -> 현재 기어의 오른쪽 톱니 (인덱스 2), 오른쪽 기어의 왼쪽 톱니 (인덱스 6)
    for i in range(idx, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotations[i+1] = -rotations[i]
        else:
            break
    
    # 회전 적용
    # 전파 과정은 원래 상태 기준으로 모두 마치고, 그 다음에 모든 회전을 적용
    for i in range(4):
        if rotations[i] == 1:
            gears[i].rotate(1)
        elif rotations[i] == -1:
            gears[i].rotate(-1)
    
# 점수 계산
# 각 기어의 인덱스 0가 1이면 점수
score = 0

for i in range(4):
    if gears[i][0] == 1: # 12시 톱니(0번 인덱스가 S극 이라면)
        score += pow(2, i)

print(score)