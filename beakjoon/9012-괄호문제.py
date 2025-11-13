def is_vps(str):
    stack = []
    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

n = int(input())
for _ in range(n):
    print(is_vps(input().strip()))