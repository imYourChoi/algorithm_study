# https://www.acmicpc.net/problem/1956

import sys
input = sys.stdin.readline

V,E = map(int,input().split())
village = [{} for _ in range(V+1)]
inf = float('inf')

for _ in range(E):
    a,b,c = map(int, input().split())
    village[a][b] = c

for via in range(V+1):
    for start in range(V+1):
        for end in range(V+1):
            village[start][end] = min(
                village[start].get(end, inf),
                village[start].get(via, inf) + village[via].get(end, inf)
            )

answer = inf

for idx, key in enumerate(village):
    answer = min(answer, key[idx])

print(answer if answer != inf else -1)