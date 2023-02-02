# https://www.acmicpc.net/problem/1967

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
n = int(input())
graph = [{} for _ in range(n+1)]

for _ in range(n-1):
    p,c,w = map(int, input().split())
    graph[p][c] = w
answer = 0

def dfs(current):
    global answer
    twoSide = []
    oneSide = 0
    for node, weight in graph[current].items():
        val = dfs(node)
        twoSide.append(val + weight)
        oneSide = max(oneSide, val + weight)
    answer = max(answer, sum(sorted(twoSide)[-2:]))
    return oneSide

dfs(1)
print(answer)
# visited = []
# def dfs(current, diameter):
#     for node in graph[current]:
#         if not visited[node]:
#             visited[node] = True
#             dfs(node, diameter + graph[current][node])
#         else:
#             global answer
#             answer = max(answer, diameter)

# for i in range(n-1):
#     visited = [False for _ in range(n+1)]
#     visited[i] = True
#     dfs(i, 0)