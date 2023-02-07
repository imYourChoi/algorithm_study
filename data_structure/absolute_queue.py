# https://www.acmicpc.net/problem/11286

# from collections import deque
import heapq
import sys
input = sys.stdin.readline

heap = []
store = {}
ans = []
for i in range(int(input())):
    n = int(input())
    if n:
        if n in store and store[n]:
            store[n] += 1
        else:
            heapq.heappush(heap, abs(n))
            store[n] = 1
    else:
        if not heap:
            ans.append(0)
        else:
            absVal = heap[0]
            # print(absVal)
            if -absVal in store and store[-absVal]:
                store[-absVal] -= 1
                ans.append(-absVal)
                if not store[-absVal]:
                    heapq.heappop(heap)
            elif absVal in store and store[absVal]:
                store[absVal] -= 1
                ans.append(absVal)
                if not store[absVal]:
                    heapq.heappop(heap)
    # print(heap)
if ans:
    print(*ans, sep='\n')

