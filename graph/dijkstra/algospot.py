# https://www.acmicpc.net/problem/1261

from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

M, N = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0

queue = deque([(0, 0)])
while queue:
    y, x = queue.popleft()
    for dy, dx in directions:
        Y, X = y+dy, x+dx
        if 0 <= Y < N and 0 <= X < M:
            if dist[Y][X] == -1:
                if maze[Y][X] == 0:
                    dist[Y][X] = dist[y][x]
                    queue.appendleft((Y, X))
                else:
                    dist[Y][X] = dist[y][x] + 1
                    queue.append((Y, X))

print(dist[-1][-1])
