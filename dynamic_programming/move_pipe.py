# https://www.acmicpc.net/problem/17070

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
# 0 = left, 1 = leftTop, 2 = Top
dp[0][1][0] = 1

for i in range(2,N):
    if not house[0][i]:
        dp[0][i][0] = dp[0][i-1][0]

for r in range(1,N):
    for c in range(2,N):
        if house[r][c]:
            continue
        if not house[r-1][c] and not house[r][c-1]:
            dp[r][c][1] = sum(dp[r-1][c-1])
        dp[r][c][0] = sum(dp[r][c-1][0:2])
        dp[r][c][2] = sum(dp[r-1][c][1:3])

print(sum(dp[-1][-1]))