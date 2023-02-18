# https://www.acmicpc.net/problem/2096

import sys
input = sys.stdin.readline

n = int(input())
min_dp = list(map(int, input().split()))
max_dp = min_dp.copy()

for nextRow in range(n-1):
    nextRow = list(map(int, input().split()))
    min_dp = [min(min_dp[0:2])+nextRow[0], min(min_dp)+ nextRow[1], min(min_dp[1:3])+nextRow[2]]
    max_dp = [max(max_dp[0:2])+nextRow[0], max(max_dp)+ nextRow[1], max(max_dp[1:3])+nextRow[2]]
print(max(max_dp), min(min_dp))