# https://www.acmicpc.net/problem/2565

import bisect

n = int(input())

arr = [*map(lambda x: x[1],sorted([list(map(int, input().split())) for _ in range(n)]))]

dp = [arr[0]]

for i in range(1,n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(n-len(dp))