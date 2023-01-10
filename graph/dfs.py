# https://www.acmicpc.net/problem/24479

import sys
sys.setrecursionlimit(10 ** 8)
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [[False, 0] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, visited, i, order):
    temp = order + 1
    visited[i][0] = True
    visited[i][1] = order

    for node in sorted(graph[i]):
        if not visited[node][0]:
            temp = dfs(graph, visited, node, temp)
    return temp

dfs(graph, visited, R, 1)

for visit in visited[1:]:
    print(visit[1])