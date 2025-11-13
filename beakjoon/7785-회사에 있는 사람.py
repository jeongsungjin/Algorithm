n = int(input())
people = {} # 딕셔러니 이용,,

for _ in range(n):
    name, action = input().split()

    if action == "enter":
        people[name] = True
    elif action == "leave":
        if name in people:
            del people[name]

for name in sorted(people.keys(), reverse=True):
    print(name)