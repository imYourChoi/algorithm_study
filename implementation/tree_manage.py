# https://www.acmicpc.net/problem/16235

from collections import deque
import sys
input = sys.stdin.readline


N, M, K = map(int, input().split(" "))
A = [list(map(int, input().split(" "))) for _ in range(N)]
land = [[5] * N for _ in range(N)]
treeArray = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    x, y, z = map(int, input().split())
    treeArray[x-1][y-1].append(z)

for x in range(N):
    for y in range(N):
        treeArray[x][y] = deque(sorted(treeArray[x][y]))

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def isValid(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def solve():
    for year in range(K):
        for r in range(N):
            for c in range(N):
                count = 0
                length = len(treeArray[r][c])

                for i in range(length):
                    tree = treeArray[r][c][i]

                    if land[r][c] < tree:
                        break
                    else:
                        land[r][c] -= tree
                        treeArray[r][c][i] += 1
                        count += 1

                for x in range(length - count):
                    land[r][c] += treeArray[r][c].pop() // 2

        for r in range(N):
            for c in range(N):
                trees = treeArray[r][c]
                for tree in trees:
                    if tree % 5 == 0:
                        for t in range(8):
                            if not isValid(r+dx[t], c + dy[t]):
                                continue
                            treeArray[r+dx[t]][c+dy[t]].appendleft(1)

                land[r][c] += A[r][c]


solve()

print(sum([sum(map(lambda x: len(x), row)) for row in treeArray]))
