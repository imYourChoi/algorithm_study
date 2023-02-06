# https://www.acmicpc.net/problem/1654

import sys
input=sys.stdin.readline
k,n=map(int, input().split())
lans=[int(input()) for _ in range(k)]

start = 1
end = sum(lans) // n

while start <= end:
    mid = (start + end)//2
    temp = 0
    for lan in lans:
        temp += lan // mid
    if temp >= n:
        start = mid+1
    else:
        end = mid-1
print(end)

# answer = 0
# while start <= end:
#     mid = (start + end)//2
#     temp = 0
#     if start == mid:
#         for lan in lans:
#             temp += lan // (mid+1)
#         if temp >= n:
#             answer = mid+1
#         else:
#             answer = mid
#         break
#     for lan in lans:
#         temp += lan // mid
#     # print([start, mid, end], temp)
#     if temp >= n:
#         start = mid
#     else:
#         end = mid-1
#     answer = mid
# print(answer)