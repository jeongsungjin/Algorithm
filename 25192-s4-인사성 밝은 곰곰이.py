import sys

input = sys.stdin.readline

N = int(input())

seen = set()
count = 0

for _ in range(N):
    msg = input().strip()
    if msg == "ENTER":
        seen = set()
    elif msg not in seen:
        seen.add(msg)
        count += 1

print(count)