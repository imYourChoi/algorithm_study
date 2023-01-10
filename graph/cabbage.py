# https://www.acmicpc.net/problem/1012

from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
answer = []
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(array, visited, tempC, tempR, column, row):
    visited[tempR][tempC] = True
    queue = deque([[tempR, tempC]])

    while queue:
        current = queue.popleft()
        for upDown, leftRight in directions:
            r = current[0] + upDown
            l = current[1] + leftRight
            if not -1 < r < row or not -1 < l < column:
                continue
            if visited[r][l] or not array[r][l]:
                continue
            visited[r][l] = True
            queue.append([r, l])

def traverse(array, column, row):
    visited = [[False]*column for _ in range(row)]
    temp = 0
    for r in range(row):
        for c in range(column):
            if not array[r][c] or visited[r][c]:
                continue
            bfs(array, visited, c, r, column, row)
            temp += 1
    return temp

for _ in range(T):
    M, N, K = map(int, input().split())
    array=[[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        array[Y][X] = 1
    answer.append(traverse(array, M, N))

for a in answer:
    print(a)