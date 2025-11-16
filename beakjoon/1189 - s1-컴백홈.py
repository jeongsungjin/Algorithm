import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())
# 도달하는 데 까지 걸리는 거리가 K인 경로의 가지 수

graph = [list(map(str, input().strip())) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
answer = 0


dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(x, y, dist):
    global answer

    if x == 0 and y == C - 1:
        if dist == K:
            answer += 1
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < R and 0 <= ny < C): # 맵 범위 밖 패스
            continue

        if visited[nx][ny] or graph[nx][ny] == 'T': # 이미 방문 했거나, 막힌 노드라면 패스
            continue
        
        visited[nx][ny] = True
        dfs(nx, ny, dist + 1)
        visited[nx][ny] = False # 백트래킹


visited[R - 1][0] = True
dfs(R - 1, 0, 1)
print(answer)


    