#4(정점개수) 5(간선개수) 1(시작 정점 번호)
#1-> 2
#ㅣㅣ_ㅣ
#3---4, 무방향 간선
import sys
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

visited_dfs = [False] * (n + 1)
dfs(v, visited_dfs)
print()
bfs(v)