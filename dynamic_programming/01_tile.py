# https://www.acmicpc.net/problem/1904

n = int(input())

dp = [0, 1, 2]
for i in range(3,n+1):
    dp.append((dp[i-2] + dp[i-1]) % 15746)
print(dp[n])