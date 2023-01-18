# https://www.acmicpc.net/problem/1912

n = int(input())
arr = list(map(int, input().split()))

dp = [(arr[0], arr[0])]

for i in range(1,n):
    cur_sum = dp[-1][1] + arr[i]
    if cur_sum <= arr[i]:
        dp.append((arr[i], arr[i]))
    elif dp[-1][0] <= cur_sum:
        dp.append((cur_sum, cur_sum))
    elif cur_sum < dp[-1][0]:
        dp.append((dp[-1][0], cur_sum))
    elif cur_sum < dp[-1][1]:
        dp.append((dp[-1][1], cur_sum))

print(max(dp)[0])

# dp = [{}] + [{i:arr[i]} for i in range(1,n+1)]

# for i in range(2,n+1):
#     for j in range(1,n-i+2):
#         dp[j][j+i-1] = max(dp[j][j+i-2], dp[j+1][j+i-1], sum(arr[j:j+i]))

# print(dp[1][n])