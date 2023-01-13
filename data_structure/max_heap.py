# https://www.acmicpc.net/problem/11279

import sys, heapq
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    op = int(input())
    if not op:
        if not array:
            print(0)
        else:
            print(heapq.heappop(array)[1])
    else:
        heapq.heappush(array, (-op, op))