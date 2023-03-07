# https://www.acmicpc.net/problem/13460

from collections import deque

N,M = map(int, input().split())
board = [list(input()) for _ in range(N)]
directions = [(-1,0),(0,1),(1,0),(0,-1)]
queue = deque([])
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def init():
    Ry, Rx, By, Bx = 0, 0, 0, 0  # 초기화
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                Ry, Rx = i, j
            elif board[i][j] == 'B':
                By, Bx = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append((Ry, Rx, By, Bx, 1))
    visited[Ry][Rx][By][Bx] = True

def move(y,x,dy,dx):
    count = 0
    while board[y+dy][x+dx] != "#" and board[y][x] != "O":
        y += dy
        x += dx
        count += 1
    return y,x,count

def solve():
    init()
    while queue:
        Ry, Rx, By, Bx, count = queue.popleft()
        if count > 10:
            return -1
        for dy,dx in directions:
            newRy, newRx, Rcount = move(Ry, Rx, dy, dx)
            newBy, newBx, Bcount = move(By, Bx, dy, dx)
            if board[newBy][newBx] == "O":
                continue
            if board[newRy][newRx] == "O":
                return count
            if newRx == newBx and newRy == newBy:
                if Rcount > Bcount:
                    newRx -= dx
                    newRy -= dy
                else:
                    newBx -= dx
                    newBy -= dy
            if not visited[newRy][newRx][newBy][newBx]:
                visited[newRy][newRx][newBy][newBx] = True
                queue.append((newRy, newRx, newBy, newBx, count + 1))
    return -1

print(solve())