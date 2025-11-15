import sys

input = sys.stdin.readline

N = int(input())

weight = list(map(int, input().split()))
weight.sort()

target = 1
for w in weight:
    if w <= target:
        target += w
    else:
        break
# 1 2 3 5 8 14 21
print(target)

