# https://www.acmicpc.net/problem/14938

n,m,r = map(int, input().split())
items = {i+1:x for i,x in enumerate(list(map(int, input().split())))}
ground = [{} for _ in range(n+1)]
inf = float('inf')

for _ in range(r):
    a,b,l = map(int, input().split())
    ground[a][b] = l
    ground[b][a] = l

for via in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            if start == end:
                continue
            if via not in ground[start] or end not in ground[via]:
                continue
            if (L := ground[start][via] + ground[via][end]) < ground[start].get(end, inf):
                if L <= m:
                    ground[start][end] = L

answer = 0

for idx, dropped in enumerate(ground[1:]):
    temp = items[idx+1]
    for key, value in dropped.items():
        if value <= m:
            temp += items[key]
    answer = max(answer, temp)

print(answer)