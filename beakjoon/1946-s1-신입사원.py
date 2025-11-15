import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = []

    for _ in range(N):
        s, m = map(int, input().split())
        score.append((s, m))
    
    score.sort() # 서류 등수 기준 정렬

    # 1 2 3 4 5
    # 4 3 2 1 5
    # 면접 등수가 앞에 것 보다 낮으면 합격
    count = 0
    current_m_rank = 100001

    # print(score[0])

    for s, m in score:
        if m < current_m_rank:
            current_m_rank = m
            count += 1
    
    print(count)
    
