import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

lights = list(map(int, input().split()))
# 2 4
def can_lihgt(h):
    pos = 0

    for x in lights:
        if x - h > pos:
            return False
        pos = x + h

    return pos >= N

left, right = 0, N
answer = N

while left <= right:
    mid = (left + right) // 2

    if can_lihgt(mid):
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)