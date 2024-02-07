# https://www.acmicpc.net/problem/14226

from collections import deque

S = int(input())
distances = [[-1] * (S+1) for _ in range(S+1)]

queue = deque()
queue.append((1, 0))
distances[1][0] = 0

while queue:
    s, c = queue.popleft()
    if distances[s][s] == -1:
        distances[s][s] = distances[s][c] + 1
        queue.append((s, s))
    if s+c <= S and distances[s+c][c] == -1:
        distances[s+c][c] = distances[s][c] + 1
        queue.append((s+c, c))
    if s >= 1 and distances[s-1][c] == -1:
        distances[s-1][c] = distances[s][c] + 1
        queue.append((s-1, c))


answer = min(filter(lambda x: x != -1, distances[S]))
print(answer)
