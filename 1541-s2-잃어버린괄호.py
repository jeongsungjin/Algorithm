s = input().strip()

# - 뒤로 다 괄호 때리면 됨??

group = s.split('-') # -을 기준으로 반띵! 앞뒤


result = sum(map(int, group[0].split('+')))

for g in group[1:]:
    result -= sum(map(int, g.split('+')))

print(result)

