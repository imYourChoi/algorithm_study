# https://www.acmicpc.net/problem/1260

from collections import deque
import sys
sys.setrecursionlimit(10 ** 8)
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

visitedD = [False for _ in range(N+1)]
visitedB = [False for _ in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, visited, i):
    visited[i] = True
    print(i, end=" ")
    for node in sorted(graph[i]):
        if not visited[node]:
            dfs(graph, visited, node)

def bfs(graph, visited, i):
    visited[i] = True
    queue = deque([i])

    while queue:
        pop = queue.popleft()
        print(pop, end=" ")
        for node in sorted(graph[pop]):
            if not visited[node]:
                visited[node] = True
                queue.append(node)

dfs(graph, visitedD, V)
print()
bfs(graph, visitedB, V)
print()