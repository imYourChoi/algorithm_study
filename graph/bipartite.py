# https://www.acmicpc.net/problem/1707

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
answer = []

def bfs(array, V):

    visited = [[False, -1] for _ in range(V + 1)]
    for i in range(1, V+1):
        if visited[i][0]:
            continue
        group = 0
        queue = deque([i])
        visited[i][0] = True
        visited[i][1] = 0

        while queue:
            group = 1 - group
            for _ in range(len(queue)):
                current = queue.popleft()
                for node in array[current]:
                    if visited[node][0] and visited[node][1] != group:
                        return "NO"
                    elif not visited[node][0]:
                        visited[node][0] = True
                        visited[node][1] = group
                        queue.append(node)
    return "YES"

for _ in range(N):
    V, E = map(int, input().split())
    array = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        array[u].append(v)
        array[v].append(u)
    
    answer.append(bfs(array, V))
    
print(*answer, sep="\n")