# https://www.acmicpc.net/problem/2098
# bit_masking

N = int(input())
inf = float('inf')
dp = [[0] * (1<<N-1) for _ in range(N)]

graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(x,visited):
    if dp[x][visited] != 0:
        return dp[x][visited]

    if visited == (1<<(N-1)) - 1:
        if graph[x][0]:
            return graph[x][0]
        return inf
    
    min_dist = inf
    for i in range(1,N):
        if not graph[x][i]:
            continue
        if visited & (1<<i-1):
            continue
        dist = graph[x][i] + dfs(i, visited | (1<<(i-1)))
        min_dist = min(min_dist, dist)
    dp[x][visited] = min_dist
    
    return dp[x][visited]

print(dfs(0,0))