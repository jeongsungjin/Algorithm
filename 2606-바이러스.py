n = int(input())
m = int(input())

def dfs(node, graph, visited):
    visited[node] = True
    count = 0

    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += 1 + dfs(neighbor, graph, visited)
    
    return count

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

result = dfs(1, graph, visited)
print(result)