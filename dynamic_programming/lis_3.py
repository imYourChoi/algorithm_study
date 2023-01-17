# https://www.acmicpc.net/problem/14002

n = int(input())
arr = list(map(int, input().split()))

dp = [[1, [arr[i]]] for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i] = [dp[j][0] + 1, dp[j][1] + [arr[i]]]

print(max(dp)[0])
print(*max(dp)[1])