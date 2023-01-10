# https://www.acmicpc.net/problem/2606

from collections import deque
import sys

N = int(input())
E = int(input())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(E):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

def virusBFS(graph, visited, i):
    visited[i] = True
    queue = deque([i])

    number = 0
    while queue:
        pop = queue.popleft()
        number += 1
        for node in graph[pop]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    return number

def virusDFS(graph, visited, i, number):
    visited[i] = True
    temp = number + 1

    for node in graph[i]:
        if not visited[node]:
            temp = virusDFS(graph, visited, node, temp)
    
    return temp

# print(virusBFS(graph, visited, 1) - 1)
print(virusDFS(graph, visited, 1, 0) - 1)