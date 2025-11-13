
def infix_to_postfix(exp):
    precedence = {"+" : 1, "-": 1, "*": 2, "/": 2, "(" : 0}
    result = []
    stack = []

    for char in exp:
        if char.isalpha():
            result.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(": # 스택의 맨 위(마지막)가 여는 괄호가 아닐 동안
                result.append(stack.pop()) # 닫는 괄호의 경우 여는 괄호 나올때 까지 스택 팝해서 결과에 어팬드
            stack.pop() 
        else: # 연산자의 경우 이미 있는 것의 우선순위가 지금 들어온 것 보다 크거나 같다면, 쭉 팝하고 지금꺼 어팬드
            while stack and precedence[stack[-1]] >= precedence[char]:
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())
    
    return ''.join(result)
    
n = input().strip()
print(infix_to_postfix(n))