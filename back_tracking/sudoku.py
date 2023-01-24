# https://www.acmicpc.net/problem/2580

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(y, x) for y in range(9) for x in range(9) if sudoku[y][x] == 0]

def promising(y,x):
    possible = {x+1 for x in range(9)}

    for c in range(9):
        possible.discard(sudoku[y][c])
    for r in range(9):
        possible.discard(sudoku[r][x])
    for r in range(y//3*3, y//3*3+3):
        for c in range(x//3*3, x//3*3+3):
            possible.discard(sudoku[r][c])
    return possible


flag = False
def dfs(idx):
    global flag
    if flag:
        return

    if idx == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return
    
    else:
        y,x = zeros[idx]

        for num in promising(y,x):
            sudoku[y][x] = num
            dfs(idx+1)
            sudoku[y][x] = 0

dfs(0)

# visit = [[set([x+1 for x in range(9)]) for _ in range(9)] for _ in range(9)]

# for y, row in enumerate(sudoku):
#     for x, elem in enumerate(row):
#         if elem:
#             visit[y][x] = {}
# num = 1
# while True:
#     flag = True
#     multiple = True
#     for y, row in enumerate(sudoku):
#         for x, elem in enumerate(row):
#             if not visit[y][x]:
#                 continue
#             if not elem:
#                 flag = False
#                 temp = set([x+1 for x in range(9)])
#                 for c in range(9):
#                     temp.discard(sudoku[y][c])
#                 for r in range(9):
#                     temp.discard(sudoku[r][x])
#                 for r in range(y//3*3, y//3*3+3):
#                     for c in range(x//3*3, x//3*3+3):
#                         temp.discard(sudoku[r][c])
#                 visit[y][x] &= temp

#             if 0<len(visit[y][x])<=num:
#                 multiple = False
#                 sudoku[y][x] = visit[y][x].pop()
#                 visit[y][x] = {}
#                 num = 1
#     if flag:
#         break
#     if multiple:
#         num += 1

# for row in sudoku:
#     print(*row)

# 2 9 5 7 4 3 8 6 1
# 4 3 1 8 6 5 9 0 0
# 8 7 6 1 9 2 5 4 3
# 3 8 7 4 5 9 2 1 6
# 6 1 2 3 8 7 4 9 5
# 5 4 9 2 1 6 7 3 8
# 7 6 3 5 2 4 1 8 9
# 9 2 8 6 7 1 3 5 4
# 1 5 4 9 3 8 6 0 0

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

# 6 0 0 4 1 0 0 0 0
# 0 2 0 0 6 3 0 0 1
# 0 0 9 8 0 0 0 0 4
# 9 0 8 0 7 6 1 0 2
# 2 6 0 0 0 0 0 9 3
# 4 0 1 2 9 0 7 0 6
# 1 0 0 0 0 5 3 0 0
# 5 0 0 6 3 0 0 7 0
# 0 0 0 0 4 2 0 0 5