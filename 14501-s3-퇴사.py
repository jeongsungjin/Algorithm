import sys

input = sys.stdin.readline

N = int(input().strip())

T = [0] * (N + 1)
P = [0] * (N + 1)

for i in range(1, N + 1):
    t, p = map(int, input().split())

    T[i] = t
    P[i] = p

dp = [0] * (N + 2) # i번째 날부터 마지막 날까지 얻을 수 있는 최대 수익

for i in range(N, 0, -1):
    if i + T[i] - 1 <= N: # 일 할 수 있음
        dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]]) 
    else:
        dp[i] = dp[i + 1] # 어차피 오늘 건은 못하니 다음으로 ~

print(dp[1]) # 1일부터 있으니까 dp[1]