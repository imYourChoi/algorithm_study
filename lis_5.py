# https://www.acmicpc.net/problem/14003

import bisect

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

indices = [1] * n

for i in range(n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        indices[i] = len(dp)
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        indices[i] = idx + 1

size = max(indices)
index = indices.index(size)
seq = []

while index >= 0:
    if indices[index] == size:
        seq.append(arr[index])
        size -= 1
    index -= 1

seq.reverse()

print(len(dp))
print(*seq)