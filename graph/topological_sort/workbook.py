# https://www.acmicpc.net/problem/1766

import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

heap = []

for idx, value in enumerate(degree):
    if not value and idx:
        heapq.heappush(heap, idx)

answer = []

while heap:
    current = heapq.heappop(heap)
    toNodes = graph[current]
    answer.append(current)

    for node in toNodes:
        degree[node] -= 1
        if not degree[node]:
            heapq.heappush(heap, node)

print(*answer)
