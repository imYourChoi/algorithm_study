# https://www.acmicpc.net/problem/12865

import sys
sys.stdin.readline
n, k = map(int, input().split())

arr = [[0,0]] + [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [{} for _ in range(n+1)]

for i in range(n+1):
    weight, value = arr[i]
    for j in range(0,k+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])