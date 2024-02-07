# https://www.acmicpc.net/problem/2011

password = list(map(int, input()))
L = len(password)
dp = [0 for _ in range(L+1)]
if (password[0] == 0):
    print("0")
else:
    password = [0] + password
    dp[0] = dp[1] = 1
    for i in range(2, L+1):
        if password[i] > 0:
            dp[i] += dp[i-1]
        temp = password[i-1] * 10 + password[i]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]
    print(dp[L] % 1000000)
