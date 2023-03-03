# https://www.acmicpc.net/problem/12100

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
count = 0

def up(board):
    global count
    count += 1
    new = [[0] * n for _ in range(n)]
    for x in range(n):
        temp = []
        curr = None
        for y in range(n):
            if not board[y][x]:
                pass
            elif curr == None:
                curr = board[y][x]
            elif board[y][x] == curr:
                temp.append(curr*2)
                curr = None
            else:
                temp.append(curr)
                curr = board[y][x]
        if curr:
            temp.append(curr)
        for y,value in enumerate(temp):
            new[y][x] = value
    return new

def down(board):
    global count
    count += 1
    new = [[0] * n for _ in range(n)]
    for x in range(n-1,-1,-1):
        temp = []
        curr = None
        for y in range(n-1,-1,-1):
            if not board[y][x]:
                pass
            elif curr == None:
                curr = board[y][x]
            elif board[y][x] == curr:
                temp.append(curr*2)
                curr = None
            else:
                temp.append(curr)
                curr = board[y][x]
        if curr:
            temp.append(curr)
        for y,value in enumerate(temp):
            new[n-1-y][x] = value
    return new

def left(board):
    global count
    count += 1
    new = [[0] * n for _ in range(n)]
    for y in range(n):
        temp = []
        curr = None
        for x in range(n):
            if not board[y][x]:
                pass
            elif curr == None:
                curr = board[y][x]
            elif board[y][x] == curr:
                temp.append(curr*2)
                curr = None
            else:
                temp.append(curr)
                curr = board[y][x]
        if curr:
            temp.append(curr)
        for x,value in enumerate(temp):
            new[y][x] = value
    return new

def right(board):
    global count
    count += 1
    new = [[0] * n for _ in range(n)]
    for y in range(n-1,-1,-1):
        temp = []
        curr = None
        for x in range(n-1,-1,-1):
            if not board[y][x]:
                pass
            elif curr == None:
                curr = board[y][x]
            elif board[y][x] == curr:
                temp.append(curr*2)
                curr = None
            else:
                temp.append(curr)
                curr = board[y][x]
        if curr:
            temp.append(curr)
        for x,value in enumerate(temp):
            new[y][n-1-x] = value
    return new


def back_track(current_board, index):
    global answer
    if index == 5:
        answer = max(answer, max([max(row) for row in current_board]))
        return

    back_track(up(current_board), index + 1)
    back_track(down(current_board), index + 1)
    back_track(left(current_board), index + 1)
    back_track(right(current_board), index + 1)

back_track(board, 0)

print(answer)