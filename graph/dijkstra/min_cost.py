# https://www.acmicpc.net/problem/1916

import heapq
import sys
input = sys.stdin.readline

N, M = int(input()), int(input())
array = [{} for _ in range(N+1)]
inf = float('inf')
distance = [inf] * (N+1)

for _ in range(M):
    start, end, cost = map(int,input().split())
    if end in array[start]:
        array[start][end] = min(cost, array[start][end])
    else: array[start][end] = cost

s, e = map(int, input().split())

def min_cost(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, arrive = heapq.heappop(q)
        if distance[arrive] < dist:
            continue
        for destination, new_dist in array[arrive].items():
            temp = dist + new_dist
            if distance[destination] > temp:
                distance[destination] = temp
                heapq.heappush(q, (temp, destination))

min_cost(s)
print(distance[e])