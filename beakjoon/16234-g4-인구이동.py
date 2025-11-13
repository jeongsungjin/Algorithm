import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split()) # 격자크기, 인구 차이 범위

A = [list(map(int, input().split())) for _ in range(N)] # 초기 인구 배열

days = 0

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동 벡터

while True:
    visited = [[False] * N for _ in range(N)] # 하루 동안의 방문 기록
    moved = False # 인구 이동 발생 여부 판단 flag

    # 모든 칸을 순회하며 아직 방문하지 않은 칸에 대해서 BFS 실행
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue


            q = deque()
            q.append((i, j))
            visited[i][j] = True # 시작 칸 방문 처리
            union = [(i, j)] # 이번 연합에 속한 좌표들
            total = A[i][j] # 연합 전체 인구합

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: # 범위 ok, 방문하지 않은 국가
                        if L <= abs(A[x][y] - A[nx][ny]) <= R: # 인구 차이 범위 ok
                            visited[nx][ny] = True
                            q.append((nx, ny)) # deque에 방문 국가 저장
                            union.append((nx, ny)) # 연합 국가 좌표 저장
                            total += A[nx][ny] # 연합이니까 토탈 인구 +

            if len(union) > 1: # 연합이 한개 이상이라면
                moved = True # 이동이 일어남
                new_population = total // len(union) # 새로운 연합에 대한 평균 인구수 계산

                for x, y in union:
                    A[x][y] = new_population # 평균 인구수로 분배
            
    if not moved:
        break

    days += 1 

print(days)