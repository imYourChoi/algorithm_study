# https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
colors = [[*input()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(y,x):
    color = colors[y][x]
    if color in ["R", "G"]:
        colors[y][x] = "W"
    for dy,dx in [(-1,0), (1,0), (0,1), (0,-1)]:
        Y, X = y+dy , x+dx
        if not 0<=Y<n or not 0<=X<n or visited[Y][X]:
            continue
        if color == colors[Y][X]:
            visited[Y][X] = True
            bfs(Y,X)

normal = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(y,x)
            normal += 1

weak = 0
visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(y,x)
            weak += 1

print(normal, weak)