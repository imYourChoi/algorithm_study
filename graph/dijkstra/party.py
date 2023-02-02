# https://www.acmicpc.net/problem/1238

import sys, heapq
input = sys.stdin.readline
N, M, X = map(int, input().split())

array = [{} for _ in range(N+1)]
inf = float('inf')
distances = [inf] * (N+1)

for _ in range(M):
    s, e, t = map(int, input().split())
    array[s][e] = t

def party(place):
    heap = [(0, place)]
    distances[place] = 0

    while heap:
        cur_distance, cur_location = heapq.heappop(heap)
        if distances[cur_location] < cur_distance:
            continue

        for destination, distance in array[cur_location].items():
            temp = cur_distance + distance
            if distances[destination] > temp:
                distances[destination] = temp
                heapq.heappush(heap, (temp, destination))
    
def individual(start, X):
    ind_distances = [inf] * (N+1)
    heap = [(0, start)]
    ind_distances[start] = 0

    while heap:
        cur_distance, cur_location = heapq.heappop(heap)
        if cur_location == X:
            return cur_distance
        if ind_distances[cur_location] < cur_distance:
            continue

        for destination, distance in array[cur_location].items():
            temp = cur_distance + distance
            if ind_distances[destination] > temp:
                ind_distances[destination] = temp
                heapq.heappush(heap, (temp, destination))

party(X)

for i in range(1, N+1):
    if i == X:
        continue
    distances[i] += individual(i, X)
print(max(distances[1:]))