import sys
input = sys.stdin.read

data = input().splitlines()
N = int(data[0])
cards = set(map(int, data[1].split()))
M = int(data[2])
queries = list(map(int, data[3].split()))

result = []

for query in queries:
    if query in cards:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))
