# https://www.acmicpc.net/problem/11003

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
array = list(map(int, input().split()))

queue = deque()
answer = []

for i in range(L):
    cur = array[i]
    while queue and queue[-1] > cur:
        queue.pop()
    queue.append(cur)

    answer.append(str(queue[0]))

for i in range(L, N):
    cur = array[i]
    while queue and queue[-1] > cur:
        queue.pop()
    queue.append(cur)

    if array[i - L] == queue[0]:
        queue.popleft()

    answer.append(str(queue[0]))

print(" ".join(answer))

# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6
