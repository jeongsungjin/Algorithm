import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split()) # 정점, 간선 개수

# 무방향 그래프, 간선에 소가 있다
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

# 다익스트라 준비
INF = int(1e15)
dist = [INF] * (N + 1)
dist[1] = 0

priority_q = []
heapq.heappush(priority_q, (0, 1)) # (비용, 정점)

while priority_q:
    cur_cost, node = heapq.heappop(priority_q)

    if dist[node] < cur_cost:
        continue

    for next_node, weight in graph[node]:
        next_cost = cur_cost + weight

        if next_cost < dist[next_node]:
            dist[next_node] = next_cost
            heapq.heappush(priority_q, (next_cost, next_node))

print(dist[N])
