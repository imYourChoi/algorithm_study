# https://www.acmicpc.net/problem/1697

from collections import deque

N, M = map(int, input().split())
visited = [False] * 100001

def check(position, queue, dest):
    if 0 <= position <= 100000 and not visited[position]:
        visited[position] = True
        queue.append(position)

    if position == dest:
        return True
    else: return False

def bfs(N, M):
    if N == M:
        return 0
    second = 0
    queue = deque([N])
    visited[N] = True

    while queue:
        second += 1
        temp = False
        for _ in range(len(queue)):
            current = queue.popleft()
            temp |= check(current - 1, queue, M)
            temp |= check(current + 1, queue, M)
            temp |= check(current * 2, queue, M)
        if temp:
            return second

print(bfs(N, M))