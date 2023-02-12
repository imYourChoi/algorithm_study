# https://www.acmicpc.net/problem/9370

import sys, heapq
input = sys.stdin.readline
inf = float('inf')

for _ in range(int(input())):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    graph = [{} for _ in range(n+1)]

    for _ in range(m):
        a,b,d = map(int, input().split())
        graph[a][b] = d
        graph[b][a] = d

    candidates = sorted([int(input()) for _ in range(t)])

    def dijkstra(start, toList):
        distances = [inf] * (n+1)
        distances[start] = 0
        heap = [(0,start)]
        while heap:
            current_distance, current_location = heapq.heappop(heap)
            if distances[current_location] < current_distance:
                continue
            for destination, distance in graph[current_location].items():
                temp = current_distance + distance
                if distances[destination] > temp:
                    distances[destination] = temp
                    heapq.heappush(heap, (temp, destination))
        return {to: distances[to] for to in toList}
    
    distances = dijkstra(s, candidates + [g,h])
    betweenGH = dijkstra(g, [h])
    fromG = dijkstra(g, candidates)
    fromH = dijkstra(h, candidates)

    for candidate in candidates:
        if distances[candidate] != inf and distances[candidate] == min(distances[g] + betweenGH[h] + fromH[candidate], distances[h] + betweenGH[h] + fromG[candidate]):
            print(candidate, end=" ")
    print()