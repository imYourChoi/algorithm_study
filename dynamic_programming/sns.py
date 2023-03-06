# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0,0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(node):
    visited[node] = True
    if not len(graph[node]):
        dp[node][1] = 1
        dp[node][0] = 0
    else:
        dp[node][1] += 1
        for each in graph[node]:
            if not visited[each]:
                dfs(each)
                dp[node][1] += min(dp[each])
                dp[node][0] += dp[each][1]

dfs(1)
print(min(dp[1]))