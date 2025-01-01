# https://www.acmicpc.net/problem/1197

# import heapq
# import sys
# input = sys.stdin.readline

# V,E = map(int, input().split())
# graph = [{} for _ in range(V+1)]

# for _ in range(E):
#     a,b,c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c

# visited = [False] * (V+1)

# heap = [(0,1)]
# answer = 0

# while heap:
#     close_dist, close_node = heapq.heappop(heap)
#     if visited[close_node]:
#         continue
#     visited[close_node] = True
#     answer += close_dist

#     for node, dist in graph[close_node].items():
#         if visited[node]:
#             continue
#         heapq.heappush(heap, (dist, node))

# print(answer)

# https://velog.io/@yoopark/baekjoon-1197

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [{} for _ in range(V+1)]

edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a_parent = get_parent(a)
    b_parent = get_parent(b)

    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def check_same_parent(a, b):
    return get_parent(a) == get_parent(b)


answer = 0

for a, b, cost in edges:
    if not check_same_parent(a, b):
        union_parent(a, b)
        answer += cost

print(answer)

# 7 9
# 1 2 29
# 2 3 16
# 3 4 12
# 4 5 22
# 5 6 27
# 6 1 10
# 2 7 15
# 5 7 25
# 4 7 18

# 5 6
# 1 2 3
# 1 3 4
# 1 4 5
# 2 5 7
# 3 5 8
# 4 5 9
