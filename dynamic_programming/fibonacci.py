# https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = []
    for i in range(0,n+1):
        if i == 0:
            dp.append([1,0])
        elif i == 1:
            dp.append([0,1])
        else:
            dp.append([dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]])
    print(dp[-1][0],dp[-1][1])