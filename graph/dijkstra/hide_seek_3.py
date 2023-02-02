# https://www.acmicpc.net/problem/13549

from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001

def check(position, queue, dest):
    if 0 <= position <= 100000 and not visited[position]:
        visited[position] = True
        queue.append(position)

    if position == dest:
        return True
    else: return False

def bfs(N, K):
    if N == K:
        return 0
    second = 0
    queue = deque([N])
    visited[N] = True

    while queue:
        temp = False
        # print(queue)
        for i in range(len(queue)):
            if queue[i] == 0:
                continue
            num = queue[i] * 2
            while num <= 100000:
                # print(num)
                temp |= check(num, queue, K)
                if temp: return second
                if K < num and K < num * 2:
                    break
                num *= 2
            # print(queue)
        for _ in range(len(queue)):
            current = queue.popleft()
            temp |= check(current - 1, queue, K)
            temp |= check(current + 1, queue, K)
            
        second += 1
        if temp:
            return second

print(bfs(N, K))