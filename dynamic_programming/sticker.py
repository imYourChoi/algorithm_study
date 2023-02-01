# https://www.acmicpc.net/problem/9465

cases = int(input())

for _ in range(cases):
    n = int(input())
    scores = list(zip(map(int, input().split()),map(int, input().split())))
    if n == 1:
        print(max(scores[0]))
    elif n == 2:
        print(max(scores[0][0]+scores[1][1],scores[0][1]+scores[1][0]))
    else:
        dp = [{"top": 0, "bottom": 0} for _ in range(n)]
        dp[0]["top"] = scores[0][0]
        dp[0]["bottom"] = scores[0][1]
        dp[1]["top"] = scores[1][0] + scores[0][1]
        dp[1]["bottom"] = scores[1][1] + scores[0][0]
        for i in range(2,n):
            dp[i]["top"] = max(dp[i-1]["bottom"], dp[i-2]["bottom"]) + scores[i][0]
            dp[i]["bottom"] = max(dp[i-1]["top"], dp[i-2]["top"]) + scores[i][1]
        print(max(dp[-1]["top"], dp[-1]["bottom"]))