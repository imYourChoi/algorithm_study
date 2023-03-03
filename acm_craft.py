# https://www.acmicpc.net/problem/1005

import sys
from collections import deque
input = sys.stdin.readline
answer = []

for _ in range(int(input())):
    N,K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    dp = [0] * (N+1)
    degree = [0] * (N+1)
    graph = [set() for _ in range(N+1)]
    for _ in range(K):
        X,Y = map(int, input().split())
        graph[X].add(Y)
        degree[Y] += 1
    queue = deque([])
    for idx, value in enumerate(degree):
        if not value and idx:
            queue.append(idx)
    W = int(input())
    
    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            toNodes = graph[current]
            for node in toNodes:
                dp[node] = max(dp[node], dp[current] + times[current])
                degree[node] -= 1
                if not degree[node]:
                    queue.append(node)
    answer.append(dp[W] + times[W])

print(*answer, sep="\n")