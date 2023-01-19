# https://www.acmicpc.net/problem/9251

a,b = input(), input()

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

# def lcs(first, second):
#     if len(first) == len(second) == 1:
#         return first == second
#     if len(first) ==  1:
#         return lcs(first, second[:-1]) + (first == second[-1])
#     if len(second) == 1:
#         return lcs(first[:-1], second) + (second == first[-1])

#     if first[-1] == second[-1]:
#         if dp[len(first)-1][len(second)-1]:
#             return dp[len(first)-1][len(second)-1]
#         result = lcs(first[:-1], second[:-1]) + 1
#         dp[len(first)-1][len(second)-1] = result
#         return result
#     else:
#         if dp[len(first)-1][len(second)-1]:
#             return dp[len(first)-1][len(second)-1]
#         result = max(lcs(first, second[:-1]), lcs(first[:-1], second))
#         dp[len(first)-1][len(second)-1] = result
#         return result

# print(lcs(a,b))

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i ==0 or j == 0:
            dp[i][j] = 0
        elif a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])