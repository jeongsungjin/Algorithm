import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
fish = list(map(int, input().split()))

# 1. 최소 어항에 물고기 +1 (이 함수는 문제가 없습니다)
def add_fish():
    min_val = min(fish)
    for i in range(len(fish)):
        if fish[i] == min_val:
            fish[i] += 1

# 2. 어항 쌓기 (공중부양)
def rotate_and_stack():
    # 2-1. 가장 왼쪽 어항을 오른쪽 위에 올림
    # 초기에 2x1 블록으로 시작
    stack = [[fish[0]]]
    line = fish[1:]
    
    #deque를 사용하면 popleft()를 O(1)에 할 수 있어 효율적
    stack[0].append(line.pop(0))
    stack = [stack[0][::-1]] + [line] # 첫 번째 회전 및 쌓기 미리 수행

    while True:
        h = len(stack)
        w = len(stack[0])

        # 남은 line의 길이가 쌓인 어항의 높이보다 작으면 중단
        if len(stack[-1]) - w < h:
            break

        # 2-2. 2층 이상인 어항들을 90도 회전
        block_to_rotate = []
        for i in range(h):
            row = []
            for j in range(w):
                row.append(stack[i][j])
            block_to_rotate.append(row)
        
        # 나머지 어항에서 쌓을 바닥 부분 분리
        remaining_line = stack[-1][w:]
        
        # 90도 시계방향 회전
        rotated_block = list(zip(*block_to_rotate[::-1]))

        # 2-3. 회전시킨 블록을 나머지 어항 위에 쌓기
        new_stack = []
        for i in range(len(rotated_block)):
            new_stack.append(list(rotated_block[i]))
        new_stack.append(remaining_line)
        
        stack = new_stack

    return stack

# 3. 물고기 수 조절
def adjust_fish(arr):
    # 각 칸의 변화량을 저장할 delta 배열
    delta = [[0] * len(arr[i]) for i in range(len(arr))]
    h = len(arr)

    # 상하좌우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for r in range(h):
        for c in range(len(arr[r])):
            for i in range(4):
                nr, nc = r + dx[i], c + dy[i]
                # 배열 범위 및 유효한 칸인지 확인
                if 0 <= nr < h and 0 <= nc < len(arr[nr]):
                    # 물고기 수 차이 계산
                    diff = (arr[r][c] - arr[nr][nc]) // 5
                    if diff > 0: # 현재 칸이 더 많으면
                        delta[r][c] -= diff
                        delta[nr][nc] += diff
    
    # delta 값을 원래 배열에 한 번에 적용
    for r in range(h):
        for c in range(len(arr[r])):
            arr[r][c] += delta[r][c]
    return arr

# 4. 어항을 다시 일렬로 놓기
def flatten(arr):
    res = []
    # 가장 긴 행(바닥)의 길이를 기준으로 열 순회
    max_len = max(len(row) for row in arr)
    for c in range(max_len):
        for r in range(len(arr) - 1, -1, -1): # 아래부터 위로
            if c < len(arr[r]):
                res.append(arr[r][c])
    return res

# 5. 다시 공중 부양 작업 (두 번 접기)
def fold_and_stack(arr):
    N = len(arr)
    # 5-1. 왼쪽 N/2개를 180도 회전시켜 오른쪽 N/2개 위에 놓기
    first_fold = [arr[:N//2][::-1], arr[N//2:]]
    
    # 5-2. 왼쪽 N/4개를 180도 회전시켜 오른쪽 N/4개 위에 놓기
    left_block = [row[:N//4] for row in first_fold]
    right_block = [row[N//4:] for row in first_fold]
    
    # 180도 회전: 행 순서 뒤집고, 각 행 내용물 뒤집기
    rotated_left = [row[::-1] for row in left_block[::-1]]
    
    # 쌓기
    final_stack = rotated_left + right_block
    return final_stack

def simulate():
    global fish
    count = 0
    while True:
        if max(fish) - min(fish) <= K:
            return count

        count += 1
        
        # 1. 물고기 추가
        add_fish()
        
        # 2. 어항 쌓기
        stacked_fish = rotate_and_stack()
        
        # 3. 물고기 수 조절
        stacked_fish = adjust_fish(stacked_fish)
        
        # 4. 일렬로 놓기
        fish = flatten(stacked_fish)
        
        # 5. 두 번째 쌓기
        folded_fish = fold_and_stack(fish)
        
        # 6. 물고기 수 조절
        folded_fish = adjust_fish(folded_fish)
        
        # 7. 일렬로 놓기
        fish = flatten(folded_fish)

print(simulate())