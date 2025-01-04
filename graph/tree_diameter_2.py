# https://www.acmicpc.net/problem/1167

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    edges = list(map(int, input().rstrip().split()))
    for i in range(1, len(edges) // 2):
        end = edges[i*2-1]
        weight = edges[i*2]
        graph[edges[0]].append((end, weight))

visited = [False] * (v+1)
answer = 0


def dfs(node):
    global answer
    visited[node] = True
    oneSide = 0
    left = 0
    right = 0
    for child, weight in graph[node]:
        if visited[child]:
            continue
        val = dfs(child)
        if left <= right:
            left = max(left, val + weight)
        else:
            right = max(right, val + weight)
        oneSide = max(oneSide, val + weight)
    answer = max(answer, left+right)
    return oneSide


dfs(1)
print(answer)

# 5
# 1 2 7 3 2 5 10 -1
# 2 1 7 -1
# 3 1 2 4 3 -1
# 4 3 3 -1
# 5 1 10 -1
