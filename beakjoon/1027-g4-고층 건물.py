import sys

input = sys.stdin.readline

N = int(input())

buildings = list(map(int, input().split()))

print(buildings)

# 두 점을 이은 기울기가 중간에 안잘려야 볼수있음. 좌우 동일
# i 번째 건물에서 j번째 건물을 바라 볼때 그 사이를 건물이 자르면 못봄
# 현재까지 본 최대 기울기보다 기울기가 작으면 안보임 (더 아래에 있어서 가려져서 안보임)
# (building[j] - buildings[i])/(ind(j) - ind(i))

answer = 0

for i in range(N):
    count = 0

    # 오른쪽 방향
    max_slope = float('-inf')

    for j in range(i + 1, N):
        slope = (buildings[j] - buildings[i]) / (j - i)
        if slope > max_slope:
            max_slope = slope
            count += 1 # 지금 기울기가 더 크다! 보인다는 뜻
    
    # 왼쪽 방향
    max_slope = float('-inf')
    for j in range(i - 1, -1, -1):
        slope = (buildings[j] - buildings[i])/(i - j)
        if slope > max_slope:
            max_slope = slope
            count += 1
    
    answer = max(count, answer)
    
print(answer)
