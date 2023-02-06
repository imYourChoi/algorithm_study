# https://www.acmicpc.net/problem/17218

first, second = " " + input(), " " + input()
f, s = len(first), len(second)
dp = [["" for x in range(s)] for y in range(f)]

for i in range(f):
    for j in range(s):
        if i==0 or j==0:
            pass
        elif first[i] == second[j]:
            dp[i][j] = dp[i-1][j-1] + first[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(dp[-1][-1])