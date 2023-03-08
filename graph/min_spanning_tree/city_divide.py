# https://www.acmicpc.net/problem/1647

import heapq
import sys
input = sys.stdin.readline

V,E = map(int, input().split())
graph = [{} for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

visited = [False] * (V+1)

heap = [(0,1)]
answer = 0
maximum = 0

while heap:
    close_dist, close_node = heapq.heappop(heap)
    if visited[close_node]:
        continue
    visited[close_node] = True
    answer += close_dist
    maximum = max(maximum, close_dist)

    for node, dist in graph[close_node].items():
        if visited[node]:
            continue
        heapq.heappush(heap, (dist, node))

print(answer - maximum)