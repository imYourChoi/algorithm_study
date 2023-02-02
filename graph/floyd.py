# https://www.acmicpc.net/problem/11404

import sys
input = sys.stdin.readline
n,m = int(input()), int(input())
distances = [{} for _ in range(n+1)]
inf = float('inf')

for _ in range(m):
    a,b,c = map(int,input().split())
    distances[a][b]=min(distances[a].get(b, inf), c)

for via in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            if start == end:
                distances[start][end] = 0
            else:
                distances[start][end] = min(
                    distances[start].get(end, inf),
                    distances[start].get(via, inf) + distances[via].get(end, inf)
                    )

for row in distances[1:]:
    for elem in sorted(row.keys()):
        if row[elem] == inf:
            print(0, end=" ")
        else:
            print(row[elem], end=" ")
    print()