import sys

input = sys.stdin.readline

N, M = map(int, input().split())
titles = []

for _ in range(N):
    name, power = input().split()
    titles.append((int(power), name)) # 튜플로 묶어서

powers = [int(input()) for _ in range(M)]

def find_title(power): # 이진 탐색!!
    left, right = 0, N - 1 # N은 칭호의 개수
    while left <= right: 
        mid = (left + right) // 2
        if titles[mid][0] < power: # 현재 가운데의 파워가 판별 대상 파워보다 작다면, 
            left = mid + 1 
        else:
            right = mid - 1
    
    return titles[left][1] # 칭호 반환

for power in powers:
    print(find_title(power))