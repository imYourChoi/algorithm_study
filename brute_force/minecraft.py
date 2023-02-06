# https://www.acmicpc.net/problem/18111

from collections import Counter

n,m,b = map(int, input().split())
ground = []
for _ in range(n): ground += map(int, input().split())

mini = min(ground)
maxi = max(ground)
_sum = sum(ground)
ground = dict(Counter(ground))

time = float('inf')
height = 0

for curHeight in range(mini, maxi+1):
    if _sum + b < curHeight * n * m:
        continue
    tempTime = 0
    for key, count in ground.items():
        if key < curHeight:
            tempTime += (curHeight - key) * count
        else:
            tempTime += (key - curHeight) * count * 2
    if tempTime <= time:
        time = tempTime
        height = curHeight

print(time, height)

# n,m,b = map(int, input().split())
# ground = [list(map(int, input().split())) for _ in range(n)]

# maxi = max([max(row) for row in ground])
# mini = min([min(row) for row in ground])
# time = float('inf')
# height = 0

# for curHeight in range(mini,maxi+1):
#     tempTime = 0
#     tempBlock = b
#     for row in ground:
#         for block in row:
#             if block < curHeight:
#                 tempBlock -= curHeight - block
#                 tempTime += curHeight - block
#             else:
#                 tempTime += (block - curHeight) * 2
#                 tempBlock += block - curHeight
#     if tempBlock < 0:
#         continue
#     else:
#         if tempTime <= time:
#             time = tempTime
#             height = curHeight

# print(time, height)