# https://www.acmicpc.net/problem/2156

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)
dp[1] = arr[1]
if len(arr) > 2:
    dp[2] = arr[1]+arr[2]
for i in range(3,len(arr)):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i], arr[i-1] + arr[i] + dp[i-3])
print(dp[-1])

# arr = [0] + [int(input()) for _ in range(int(input()))]
# dp = [0, arr[1]] 
# if len(arr) > 2:
#     dp.append(arr[1]+arr[2])
# for i in range(3,len(arr)):
#     temp = dp[i-2] + arr[i]
#     oneBefore = arr[i-1] + arr[i] + max(dp[0:i-2])
#     dp.append(max(temp, oneBefore))
# print(max(dp))