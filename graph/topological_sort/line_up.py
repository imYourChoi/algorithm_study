# https://www.acmicpc.net/problem/2252

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    A,B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

queue = deque([])

for idx, value in enumerate(degree):
    if not value and idx:
        queue.append(idx)

answer = []

while queue:
    current = queue.popleft()
    toNodes = graph[current]
    answer.append(current)

    for node in toNodes:
        degree[node] -= 1
        if not degree[node]:
            queue.append(node)

print(*answer)