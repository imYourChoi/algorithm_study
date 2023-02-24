# https://www.acmicpc.net/problem/14502

import itertools
from collections import deque

N,M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
empty = []
virus = []
for y, row in enumerate(lab):
    for x, space in enumerate(row):
        if not space:
            empty.append((y,x))
        elif space == 2:
            virus.append((y,x))
emptyLen = len(empty)

def bfs():
    queue = deque(virus)
    visited = set()
    while queue:
        for _ in range(len(queue)):
            y,x = queue.popleft()
            for dy,dx in [(-1,0), (0,1), (1,0), (0,-1)]:
                Y,X = y+dy, x+dx
                if not 0<=Y<N or not 0<=X<M:
                    continue
                if lab[Y][X] or (Y,X) in visited:
                    continue
                visited.add((Y,X))
                queue.append((Y,X))
    
    return emptyLen - len(visited) - 3



answer = 0

for comb in itertools.combinations(empty, 3):
    for Y,X in comb:
        lab[Y][X] = 1
    answer = max(answer, bfs())
    for Y,X in comb:
        lab[Y][X] = 0

print(answer)