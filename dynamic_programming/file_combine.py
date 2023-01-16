# https://www.acmicpc.net/problem/11066

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    inf = float('inf')
    arr = [0] + list(map(int, input().split()))

    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1,n):
        dp[i][i+1] = arr[i] + arr[i+1]

    for i in range(3,n+1):
        for j in range(1,n-i+2):
            if i == 1 or i == 2:
                continue
            temp = inf
            for k in range(1, i):
                add = dp[j][j+k-1] + dp[j+k][j+i-1]
                temp = min(temp, add)
            dp[j][j+i-1] = temp + sum(arr[j:j+i])
    
    print(dp[1][-1])