# https://www.acmicpc.net/problem/11657

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
buses = [{} for _ in range(n+1)]
edges = []

inf = float('inf')
for _ in range(m):
    edges.append(list(map(int, input().rstrip().split())))

def bellman_ford(start):
    dist = [inf] * (n+1)
    dist[start] = 0
    
    for i in range(n):
        for a,b,c in edges:
            if dist[a] != inf and dist[a] + c < dist[b]:
                dist[b] = dist[a] + c

                if i == n-1:
                    return -1
    return dist

answer = bellman_ford(1)
if answer == -1:
    print(answer)
else:
    for dist in answer[2:]:
        if dist == inf:
            print(-1)
        else:
            print(dist)