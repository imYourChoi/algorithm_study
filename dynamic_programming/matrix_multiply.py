# https://www.acmicpc.net/problem/11049

n = int(input())

inf = float('inf')
arr = [0] + [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1,n):
    dp[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1]

for i in range(3,n+1):
    for j in range(1,n-i+2):
        if i == 1 or i == 2:
            continue
        temp = inf
        for k in range(1, i):
            add = dp[j][j+k-1] + dp[j+k][j+i-1] + arr[j][0]*arr[j+k-1][1]*arr[j+i-1][1]
            temp = min(temp, add)
        dp[j][j+i-1] = temp 

print(dp[1][-1])

# arr = [list(map(int, input().split())) for _ in range(n)]
# arr = [a for a, _ in arr] + [arr[-1][1]]
# dp = [[0] * n for _ in range(n)]

# for step in range(1,n):
#     for loc in range(n-step):
#         end = loc + step
#         mul = arr[loc] * arr[end+1]
#         minimum =  min(yk + xk + sz * mul for yk, xk, sz in zip(dp[loc][loc:end], dp[end][loc+1:end+1], arr[loc+1:end+1]))
#         dp[loc][end] = dp[end][loc] = minimum

# print(dp[0][-1])