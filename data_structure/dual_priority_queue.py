# https://www.acmicpc.net/problem/7662

import sys, heapq
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    count = int(input())
    minHeap = []
    maxHeap = []
    store = {}

    for _ in range(count):
        op = input().rstrip()

        if op.startswith("I"):
            _, num = op.split()
            num = int(num)
            heapq.heappush(minHeap, num)
            heapq.heappush(maxHeap, (-num, num))
            if num in store:
                store[num] += 1
            else: store[num] = 1
        
        if op == "D 1":
            if not maxHeap:
                continue
            pop = heapq.heappop(maxHeap)[1]
            while not store[pop]:
                if not maxHeap:
                    break
                pop = heapq.heappop(maxHeap)[1]
            if store[pop]:
                store[pop] -= 1
        
        if op == "D -1":
            if not minHeap:
                continue
            pop = heapq.heappop(minHeap)
            while not store[pop]:
                if not minHeap:
                    break
                pop = heapq.heappop(minHeap)
            if store[pop]:
                store[pop] -= 1
    
    if not maxHeap or not minHeap:
        print("EMPTY")
    else:
        flag = False
        maxV = heapq.heappop(maxHeap)[1]
        minV = heapq.heappop(minHeap)
        while not store[maxV]:
            if not maxHeap:
                print("EMPTY")
                flag = True
                break
            maxV = heapq.heappop(maxHeap)[1]
        if flag:
            continue
        print(maxV, end=" ")
        while not store[minV]:
            minV = heapq.heappop(minHeap)
        print(minV)