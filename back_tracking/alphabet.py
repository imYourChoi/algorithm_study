# https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline

R,C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
directions = [(-1, 0), (0,-1), (0,1), (1,0)]

answer = 1

def dfs(y,x,path):
    global answer
    stack = set([(0, 0, board[0][0])])
    while stack :
        y, x, path = stack.pop()
        answer = max(answer, len(path))
        if answer == 26 :
            break
        for dy, dx in directions:
            Y,X = y+dy, x+dx
            if 0 <= Y < R and 0<= X < C and board[Y][X] not in path:       
                stack.add((Y, X, path + board[Y][X]))

dfs(0,0,board[0][0])
print(answer)

# R,C = map(int, input().split())

# board = [list(input()) for _ in range(R)]
# directions = [(-1, 0), (0,-1), (0,1), (1,0)]

# visited = [[False] * C for _ in range(R)]
# visited[0][0] = True
# path = [False] * 26
# path[ord(board[0][0]) - 65] = True

# answer = 1

# def dfs(y,x,count):
#     global answer
#     if count > answer:
#         answer = count
#     for dy, dx in directions:
#         Y,X = y+dy, x+dx
#         if not 0<=Y<R or not 0<=X<C:
#             continue
#         if visited[Y][X] or path[ord(board[Y][X])-65]:
#             continue
#         visited[Y][X] = True
#         path[ord(board[Y][X])-65] = True
#         dfs(Y,X,count+1)
#         visited[Y][X] = False
#         path[ord(board[Y][X])-65] = False

# dfs(0,0,1)
# print(answer)