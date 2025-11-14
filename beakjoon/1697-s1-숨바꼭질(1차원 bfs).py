import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
# 1차원 BFS
# 수빈이의 위치를 deque.append()
# while q: if 수빈 == 동생: return cnt

MAX = int(100001)
dist = [-1] * (MAX + 1)

def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0

    while q:
        x = q.popleft()

        if x == K:
            return dist[x]
        

        for nx in (x - 1, x + 1, 2*x):
            if 0 <= nx < MAX and dist[nx] == -1: # 최대 범위내이고, 방문하지 않은 점일때
                q.append(nx)
                dist[nx] = dist[x] + 1 # nx 까지의 시간 = 이전 시간 + 1
        
print(bfs(N))