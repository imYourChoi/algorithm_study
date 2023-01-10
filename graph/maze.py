# https://www.acmicpc.net/problem/2178

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = [list(map(int, [*input().rstrip()])) for _ in range(N)]

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def maze(N, M):
    way = 1
    queue = deque([[0, 0]])
    array[0][0] = 0

    while queue:
        way += 1
        for _ in range(len(queue)):
            y, x = queue.popleft()

            for dy, dx in directions:
                if y + dy == N - 1 and x + dx == M - 1:
                    return way
                if not -1 < x + dx < M or not -1 < y + dy < N:
                    continue
                if not array[y + dy][x + dx]:
                    continue
                queue.append([y + dy, x + dx])
                array[y + dy][x + dx] = 0

print(maze(N, M))