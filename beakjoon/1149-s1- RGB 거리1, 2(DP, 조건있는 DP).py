import sys

input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
answer = INF

for first_color in range(3):
    # 첫 집 외에 접근 불가 값으로 설정하기 위해 INF 설정
    dp = [[INF] * 3 for _ in range(N)]

    # 첫번째 집 색 고정
    dp[0][first_color] = cost[0][first_color]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]


    # 마지막 집 (N - 1)은 꼭 first_color와 달라야함
    for last_color in range(3):
        if last_color != first_color:
            answer = min(answer, dp[N - 1][last_color])

print(answer)

