import sys

input = sys.stdin.readline

N, K = map(int, input().split())

contry_arr = [list(map(int, input().split())) for _ in range(N)]

contry_arr.sort(key=lambda x: (-x[1], -x[2], -x[3])) # 금은동 열을 내림차순 정렬

rank_dict = {}
rank = 1

for i in range(N):
    if contry_arr[i][0] == K:
        print(rank)
        break

    if i < N - 1:
        if contry_arr[i][1:] != contry_arr[i+1][1:]:
            rank = i + 2

