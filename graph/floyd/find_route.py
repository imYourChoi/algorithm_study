# https://www.acmicpc.net/problem/11403

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for via in range(n):
    for start in range(n):
        for end in range(n):
            if graph[start][end]:
                continue
            if graph[start][via] and graph[via][end]:
                graph[start][end] = 1

for row in graph: print(*row)