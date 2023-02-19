# https://www.acmicpc.net/problem/15686

from collections import deque
from itertools import combinations

N,M = map(int, input().split())
city = []
chickens = []
houses = 0
for r in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for c, type in enumerate(row):
        if type == 2:
            chickens.append((r,c))
        elif type == 1:
            houses += 1

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def calculateDistance(oneChicken):
    queue = deque([*oneChicken])
    total = 0
    distance = 0
    count = 0
    visited = [[False] * N for _ in range(N)]
    while count < houses:
        distance += 1
        for _ in range(len(queue)):
            y,x = queue.popleft()
            for dy,dx in directions:
                Y,X = y+dy,x+dx
                if not 0<=Y<N or not 0<=X<N or visited[Y][X]:
                    continue
                visited[Y][X] = True
                if city[Y][X] == 1:
                    count += 1
                    total += distance
                queue.append((Y,X))
    return total

answer = float('inf')
comb = list(combinations(chickens, M))
for oneChicken in comb:
    answer = min(answer, calculateDistance(oneChicken))
print(answer)