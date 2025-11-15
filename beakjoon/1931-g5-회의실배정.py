import sys

input = sys.stdin.readline

N = int(input())
meetings = []

# 끝나는 시간이 빠른대로 정렬
for _ in range(N):
    s, e = map(int, input().split())

    meetings.append((e, s)) # 끝시간 앞에 넣기

meetings.sort()

count = 0
current_end = 0

for e, s in meetings:
    if s >= current_end: # 현재 종료 시간이 다음 시작 시간보다 빠르다면 
        count += 1
        current_end = e # 다음거 넣기

print(count)

