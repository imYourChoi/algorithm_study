# https://www.acmicpc.net/problem/13334

import sys, heapq
input = sys.stdin.readline

n = int(input())
bigger = []
smaller = []

for _ in range(n):
    h,o = map(int, input().split())
    if h>o: h,o = o,h
    heapq.heappush(smaller, (h,o))
    heapq.heappush(bigger, (o,h))
d = int(input())
oldLoc = smaller[0][0]
loc = smaller[0][0]
answer = 0
count = 0

while bigger:
    while bigger and bigger[0][0] <= loc + d:
        bigPop = heapq.heappop(bigger)
        if bigPop[1] >= loc:
            count += 1
    while smaller and smaller[0][0] < loc:
        smallPop = heapq.heappop(smaller)
        if smallPop[1] <= oldLoc + d:
            count -= 1
    answer = max(answer,count)
    if not bigger: continue
    oldLoc = loc
    loc = bigger[0][0] - d

print(answer)