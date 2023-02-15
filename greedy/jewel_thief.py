# https://www.acmicpc.net/problem/1202

import sys, heapq
input = sys.stdin.readline

N,K = map(int,input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
heapq.heapify(jewels)
bags = sorted([int(input()) for _ in range(K)])

temp = []
answer = 0
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        weight, value = heapq.heappop(jewels)
        heapq.heappush(temp, -value)
    if temp:
        answer += -heapq.heappop(temp)

print(answer)

# N,K = map(int,input().split())
# jewels = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1],  reverse=True)
# weights = sorted([int(input()) for _ in range(K)])
# visited = [False] * K
# count = 0
# answer = 0
# for jewel in jewels:
#     idx = bisect.bisect_left(weights, jewel[0])
#     if idx >= K:
#         continue
#     if visited[idx]:
#         while idx < K:
#             if not visited[idx]:
#                 visited[idx] = True
#                 answer += jewel[1]
#                 count += 1
#                 break
#             idx += 1
#     else:
#         visited[idx] = True
#         answer += jewel[1]
#         count += 1
#     if count == K:
#         break
# print(answer)