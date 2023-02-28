# https://www.acmicpc.net/problem/1197

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

# 7 9
# 1 2 29
# 2 3 16
# 3 4 12
# 4 5 22
# 5 6 27
# 6 1 10
# 2 7 15
# 5 7 25
# 4 7 18

# 5 6
# 1 2 3
# 1 3 4
# 1 4 5
# 2 5 7
# 3 5 8
# 4 5 9