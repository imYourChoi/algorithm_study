# https://www.acmicpc.net/problem/1655

import sys
import heapq

input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]

leftHeap = []
rightHeap = []
answer = []

for num in array:

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-num, num))
    else:
        heapq.heappush(rightHeap, (num, num))

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        min = heapq.heappop(rightHeap)[1]
        max = heapq.heappop(leftHeap)[1]
        heapq.heappush(leftHeap, (-min, min))
        heapq.heappush(rightHeap, (max, max))

    answer.append(leftHeap[0][1])

print(*answer, sep="\n")
