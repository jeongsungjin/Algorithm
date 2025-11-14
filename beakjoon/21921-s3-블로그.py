import sys

input = sys.stdin.readline

# 누적합 / 슬라이딩윈도우

N, X = map(int, input().split())

visitors = list(map(int, input().split()))

# X 길이의 최대 구간합 계산

current_sum = sum(visitors[:X])
max_sum = current_sum
count = 1

for i in range(X, N):
    current_sum += visitors[i]
    current_sum -= visitors[i - X]

    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)

