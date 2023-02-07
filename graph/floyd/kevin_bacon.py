# https://www.acmicpc.net/problem/1389

import sys
input=sys.stdin.readline

n,m = map(int, input().split())
relation = [{} for _ in range(n+1)]

for _ in range(m):
    a,b=map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1

for via in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if start == end:
                continue
            relation[start][end] = min(
                relation[start].get(end, 5001),
                relation[start].get(via, 5001) + relation[via].get(end, 5001)
            )

# print(relation)
print((a := [sum(person.values()) for person in relation[1:]]).index(min(a))+1)