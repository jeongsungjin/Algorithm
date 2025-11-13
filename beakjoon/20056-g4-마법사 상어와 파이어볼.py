import sys
from collections import defaultdict

input = sys.stdin.readline

direction = [(-1, 0), (-1, 1), (0, 1), (1, 1),
             (1, 0), (1, -1), (0, -1), (-1, -1)]

N, M, K = map(int, input().split())

fireball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

for _ in range(K):
    grid = defaultdict(list)

    # 파이어볼 이동
    for r, c, m, s, d in fireball:
        dr, dc = direction[d]
        nr = (r + dr * s) % N
        nc = (c + dc * s) % N
        grid[(nr, nc)].append((m, s, d))

    new_fireball = []

    # 이동 후 각 칸 검사
    for (r, c), items in grid.items():
        if len(items) == 1:  # 해당 좌표에 파이어볼이 1개라면
            m, s, d = items[0]
            new_fireball.append([r, c, m, s, d])
        else:
            # 2개 이상일 때
            total_m = sum(m for m, _, _ in items)
            total_s = sum(s for _, s, _ in items)
            cnt = len(items)

            new_m = total_m // 5
            if new_m == 0:
                continue
            new_s = total_s // cnt

            is_all_even = all(d % 2 == 0 for _, _, d in items)
            is_all_odd = all(d % 2 == 1 for _, _, d in items)

            if is_all_even or is_all_odd:
                new_dirs = [0, 2, 4, 6]
            else:
                new_dirs = [1, 3, 5, 7]

            for nd in new_dirs:
                new_fireball.append([r, c, new_m, new_s, nd])

    fireball = new_fireball 

print(sum(m for _, _, m, _, _ in fireball))
