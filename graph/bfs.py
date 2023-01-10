# https://www.acmicpc.net/problem/24444

from collections import deque
import sys

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [[False, 0] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, visited, i):
    visited[i][0] = True
    queue = deque([i])

    order = 0
    while queue:
        # print(queue)
        pop = queue.popleft()
        order += 1
        visited[pop][1] = order
        for node in sorted(graph[pop]):
            if not visited[node][0]:
                visited[node][0] = True
                queue.append(node)

bfs(graph, visited, R)

for visit in visited[1:]:
    print(visit[1])