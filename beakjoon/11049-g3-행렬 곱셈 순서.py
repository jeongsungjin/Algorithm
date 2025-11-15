import sys

input = sys.stdin.readline

N = int(input())
matrix_list = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] : i ~ j 까지 곱할 때의 최소 연산 비용
dp = [[0] * N for _ in range(N)]
INF = int(1e9)
# length : 부분 행렬 곱의 길이
for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = INF

        for k in range(i, j): # 분할점의 역할 왼쪽 (i...k), 오른쪽 (k+1...j)
            # 즉, 왼쪽 최적 + 오른쪽 최적 + 두 결과를 곱하는 비용으로 계산
            cost = dp[i][k] + dp[k + 1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][N - 1])