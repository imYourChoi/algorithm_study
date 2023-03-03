# https://www.acmicpc.net/problem/2623

from collections import deque

N,M = map(int, input().split())
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    order = list(map(int, input().split()))[1:]
    for i in range(len(order)-1):
        graph[order[i]].append(order[i+1])
        in_degree[order[i+1]] += 1

answer = []
queue = deque([])

for idx, value in enumerate(in_degree):
    if not value and idx:
        queue.append(idx)

while queue:
    current = queue.popleft()
    answer.append(current)
    for node in graph[current]:
        in_degree[node] -= 1
        if in_degree[node] == 0:
            queue.append(node)
if any(x>0 for x in in_degree):
    print(0)
else:
    print(*answer, sep="\n")