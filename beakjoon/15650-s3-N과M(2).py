N , M = map(int, input().split())

def dfs(start, comb):
    if len(comb) == M: #현재 숫자 조합 리스트 길이가 M이면 다고름
        print(*comb) # 현재까지 선택한 숫자 조합 리스트
        return
    
    for i in range(start, N + 1): #시작 위치부터 N을 하나씩 늘리며
        dfs(i + 1, comb + [i])

dfs(1, []) #빈 리스트
