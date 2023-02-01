# https://www.acmicpc.net/problem/11725

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [set() for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

parent[1] = True
queue = deque([1])

while queue:
    for _ in range(len(queue)):
        current = queue.popleft()
        for node in graph[current]:
            if parent[node]:
                continue
            queue.append(node)
            parent[node] = current

print(*parent[2:],sep="\n")