# https://www.acmicpc.net/problem/11779

import heapq, sys
input = sys.stdin.readline

n,m = int(input()), int(input())
graph = [{} for _ in range(n+1)]
inf = float('inf')
distance = [[inf, []] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(c, graph[a][b])
    else: graph[a][b] = c

start, end = map(int, input().split())

def min_cost(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = [0, [start]]
    
    while heap:
        cur_dist, current = heapq.heappop(heap)
        if distance[current][0] < cur_dist:
            continue
        for to, new_dist in graph[current].items():
            temp = cur_dist + new_dist
            if distance[to][0] > temp:
                distance[to][0] = temp
                distance[to][1] = distance[current][1][:] + [to]
                heapq.heappush(heap, (temp, to))

min_cost(start)
print(distance[end][0])
print(len(distance[end][1]))
print(*distance[end][1])