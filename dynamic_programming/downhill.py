# https://www.acmicpc.net/problem/1520

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

xCor, yCor = [-1, 1, 0, 0], [0, 0, 1, -1]
ways = [[-1] * N for _ in range(M)]


def downhill(x, y):
    if y == M-1 and x == N-1:
        return 1

    value = arr[y][x]
    if ways[y][x] > -1:
        return ways[y][x]
    ways[y][x] = 0
    for dx, dy in zip(xCor, yCor):
        newx, newy = x+dx, y+dy
        if 0 <= newx < N and 0 <= newy < M:
            if arr[newy][newx] < value:
                if ways[newy][newx] == 0:
                    continue
                ways[y][x] += downhill(newx, newy)
    return ways[y][x]


downhill(0, 0)
print(ways[0][0])
