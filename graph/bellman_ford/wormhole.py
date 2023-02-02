# https://www.acmicpc.net/problem/1865

import sys
input = sys.stdin.readline
inf = 10001

for _ in range(int(input())):
    n,m,w=map(int, input().split())
    edges = [{} for _ in range(n+1)]
    distances = [inf] * (n+1)
    # distances[1] = 0
    for _ in range(m):
        s,e,t=map(int, input().split())
        edges[s][e] = min(edges[s].get(e,inf),t)
        edges[e][s] = min(edges[e].get(s,inf),t)
    for _ in range(w):
        s,e,t=map(int, input().split())
        edges[s][e] = min(edges[s].get(e,0),-t)
    
    def bellman_ford():
        for j in range(n):
            for i in range(1,n+1):
                for edge, weight in edges[i].items():
                    if distances[edge] > distances[i] + weight:
                        distances[edge] = distances[i] + weight
                        if j == n-1:
                            return "YES"
        return "NO"
    
    print(bellman_ford())
