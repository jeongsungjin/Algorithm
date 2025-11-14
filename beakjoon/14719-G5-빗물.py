import sys

input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
# 3 0 1 4

total_water = 0

for i in range(1, W - 1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i + 1:])

    water = min(left_max, right_max) - blocks[i]

    if water > 0: # 현재칸이 양옆보다 높을때 음수 발생 가능
        total_water += water


print(total_water)