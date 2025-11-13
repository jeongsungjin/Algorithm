n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for num in b:
    print(1 if num in a else 0)