# https://www.acmicpc.net/problem/11054

import bisect

n = int(input())
arr = [*map(int,input().split())]

dp = [arr[0]]
dp_rev = [arr[-1]]
indices = [[1,1] for _ in range(n)] 

for i in range(1,n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        indices[i][0] = len(dp)
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
        indices[i][0] = idx + 1

for i in range(n-1,-1,-1):
    if arr[i] > dp_rev[-1]:
        dp_rev.append(arr[i])
        indices[i][1] = len(dp_rev)
    else:
        idx = bisect.bisect_left(dp_rev, arr[i])
        dp_rev[idx] = arr[i]
        indices[i][1] = idx + 1

print(sum(max(indices, key = lambda x:x[0]+x[1]))-1)