# https://www.acmicpc.net/problem/1753

import sys, heapq
input = sys.stdin.readline
V, E = map(int, input().split())
init = int(input())

array = [{} for _ in range(V+1)]
inf = float('inf')
distances = [inf] * (V+1)

for _ in range(E):
    start, end, cost = map(int,input().split())
    if end in array[start]:
        array[start][end] = min(cost, array[start][end])
    else: array[start][end] = cost

def short_path(init):
    heap = [(0, init)]
    distances[init] = 0

    while heap:
        cur_distance, cur_location = heapq.heappop(heap)
        if distances[cur_location] < cur_distance:
            continue

        for destination, distance in array[cur_location].items():
            temp_distance = cur_distance + distance
            if temp_distance < distances[destination]:
                distances[destination] = temp_distance
                heapq.heappush(heap, (temp_distance, destination))

short_path(init)

for i in distances[1:]:
    print(str(i).upper())