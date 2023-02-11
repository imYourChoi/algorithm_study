# https://www.acmicpc.net/problem/1504

import sys, heapq
input = sys.stdin.readline
N,E = map(int, input().split())
graph = [{} for _ in range(N+1)]
inf = float('inf')
distances = []

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

v1,v2 = map(int, input().split())

def specific(start, to1, to2):
    distances = [inf] * (N+1)
    heap = [(0, start)]
    distances[start] = 0

    while heap:
        cur_distance, cur_location = heapq.heappop(heap)
        if distances[cur_location] < cur_distance:
            continue

        for destination, distance in graph[cur_location].items():
            temp_distance = cur_distance + distance
            if temp_distance < distances[destination]:
                distances[destination] = temp_distance
                heapq.heappush(heap, (temp_distance, destination))
    if not to2:
        return distances[to1]
    return distances[to1], distances[to2]

toV1, toV2 = specific(1,v1,v2)
fromV1, fromV2 = specific(N,v1,v2)
between= specific(v1,v2, 0)
print(v if (v:=min(toV1 + fromV2, toV2 + fromV1) + between) != inf else -1)