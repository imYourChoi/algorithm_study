# https://www.acmicpc.net/problem/7579

n, k = map(int, input().split())

b = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
total = sum(c)
dp = [[0 for _ in range(total+1)] for _ in range(n+1)]
answer = sum(c)

for i in range(n+1):
    for j in range(total+1):
        byte = b[i]
        cost = c[i]

        if cost > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)
        
        if dp[i][j] >= k:
            answer = min(answer, j)

print(answer)