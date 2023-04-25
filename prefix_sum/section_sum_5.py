# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

n,m=map(int, input().split())
table = [list(map(int, input().rstrip().split())) for _ in range(n)]
accumulative = [[0] * n for _ in range(n)]

for y in range(n):
    for x in range(n):
        if x == 0 and y == 0:
            accumulative[y][x] = table[y][x]
        elif y == 0:
            accumulative[y][x] = accumulative[y][x-1] + table[y][x]
        elif x == 0:
            accumulative[y][x] = accumulative[y-1][x] + table[y][x]
        else:
            accumulative[y][x] = accumulative[y][x-1] + accumulative[y-1][x] - accumulative[y-1][x-1] + table[y][x]

for _ in range(m):
    x1,y1,x2,y2=map(int, input().split())
    answer = accumulative[x2-1][y2-1]
    if x1-1 and y1-1:
        answer -= accumulative[x1-2][y2-1] + accumulative[x2-1][y1-2]
        answer += accumulative[x1-2][y1-2]
    elif y1-1:
        answer -= accumulative[x2-1][y1-2]
    elif x1-1:
        answer -= accumulative[x1-2][y2-1]

    print(answer)