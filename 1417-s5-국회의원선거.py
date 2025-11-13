import heapq
from heapq import heappush as push, heappop as pop

# import sys
# input = lambda: sys.stdin.readline().strip()

n = int(input())

my_votes = int(input()) #내 표

other_votes = []

for _ in range(n - 1):
    v = int(input())
    other_votes.append(-v) #남 표

heapq.heapify(other_votes) #최대 힙

count = 0

while other_votes:
    top = -pop(other_votes)
    if top < my_votes:
        break

    top -= 1
    my_votes += 1
    count += 1
    push(other_votes, -top)

print(count)