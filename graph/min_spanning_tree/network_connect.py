# https://www.acmicpc.net/problem/1922

import heapq
import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
graph = [{} for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        continue
    graph[a][b] = c
    graph[b][a] = c

visited = [False] * (N+1)

heap = [(0, 1)]
answer = 0

while heap:
    close_dist, close_node = heapq.heappop(heap)
    if visited[close_node]:
        continue
    visited[close_node] = True
    answer += close_dist

    for node, dist in graph[close_node].items():
        if visited[node]:
            continue
        heapq.heappush(heap, (dist, node))

print(answer)
