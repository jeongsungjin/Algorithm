import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

# dp table (N+1) X (K + 1)

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1): # i 현재 물건 인덱스
    weight, value = items[i - 1] # i 번째 물건의 무게와 가치
    for w in range(1, K + 1):
        if weight <= w: # 담을 수 있다면, 담는 경우와 안담는 경우 중 큰 Value 선택
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[N][K])