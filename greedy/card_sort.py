# https://www.acmicpc.net/problem/1715

import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

heapq.heapify(cards)
answer = 0

while len(cards) > 1:
    popped1 = heapq.heappop(cards)
    popped2 = heapq.heappop(cards)
    answer += (v := popped1 + popped2)
    heapq.heappush(cards, v)
print(answer)