import sys

input = sys.stdin.readline
N = int(input())

video = [list(map(int, input().strip())) for _ in range(N)]


def compress(x, y, n):
    color = video[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if video[i][j] != color:
                half = n // 2
                return "(" + compress(x, y, half) + compress(x, y + half, half) + \
                compress(x + half, y, half) + compress(x + half, y + half, half) + ")"
    
    return str(color)

compress(0, 0, N)

print(compress(0, 0, N))
