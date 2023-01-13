# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
N, M = map(int, input().split())
array = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    array[u].append(v)
    array[v].append(u)

def dfs(i):
    visited[i] = True

    for node in array[i]:
        if not visited[node]:
            dfs(node)
    
answer = 0
for i in range(1, N+1):
    if visited[i]:
        continue
    dfs(i)
    answer += 1
print(answer)