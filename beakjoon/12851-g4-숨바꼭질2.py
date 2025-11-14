import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 100001

dist = [-1] * MAX # 해당 지점까지 걸린 시간
ways = [0] * MAX # 해당 지점 까지 도달하는 최단 경로 수

def bfs(start):
    q = deque()
    q.append(start)

    dist[start] = 0
    ways[start] = 1

    while q:
        x = q.popleft()
        for nx in (x - 1, x + 1, 2*x):
            if 0 <= nx < MAX: # 범위 내라면, 
                if dist[nx] == -1: # 첫 방문이라면, 
                    dist[nx] = dist[x] + 1
                    ways[nx] = ways[x]
                    q.append(nx)
                elif dist[nx] == dist[x] + 1: # 첫방문은 아니지만, 최단 거리 동일할때
                    ways[nx] += ways[x]

bfs(N)

print(dist[K])
print(ways[K])


            
