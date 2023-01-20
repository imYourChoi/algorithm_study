# https://www.acmicpc.net/problem/2293

n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [0 for i in range(k+1)]
dp[0] = 1

for coin in arr:
    for j in range(coin,k+1):
        dp[j] += dp[j-coin]

print(dp[k])