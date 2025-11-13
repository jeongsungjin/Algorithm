chess_pattern1 = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB'
]

chess_pattern2 = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

def count(board, x_index, y_index, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[x_index + i][y_index + j] != pattern[i][j]:
                count += 1
    return count

n, m = map(int, input().split())
board = []
for _ in range(int(n)):
    board.append(input().strip()) 

min_count = float('inf')

for i in range(int(n - 7)):
    for j in range(int(m - 7)):
        repaint1 = count(board, i, j, chess_pattern1)
        repaint2 = count(board, i, j, chess_pattern2)
        min_count = min(min_count, repaint1, repaint2)

print(min_count)
