# https://www.acmicpc.net/problem/1956

import sys, heapq
input = sys.stdin.readline

V,E = map(int,input().split())
village = [{} for _ in range(V+1)]
inf = float('inf')

for _ in range(E):
    a,b,c = map(int, input().split())
    village[a][b] = c

def exercise(start):
    distances = [inf] * (V+1)
    heap = [(0,start)]

    while heap:
        cur_distance, cur_location = heapq.heappop(heap)
        if distances[cur_location] < cur_distance:
            continue
        for destination, distance in village[cur_location].items():
            temp_distance = cur_distance + distance
            if temp_distance < distances[destination]:
                distances[destination] = temp_distance
                heapq.heappush(heap, (temp_distance, destination))
    return distances[start]

answer = inf
for i in range(1,V+1):
    answer = min(answer, exercise(i))

print(answer if answer != inf else -1)
