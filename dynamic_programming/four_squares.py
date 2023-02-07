# https://www.acmicpc.net/problem/17626

n = int(input())

# 브루트 포스
if n ** 0.5 % 1 == 0:
    print(1)
    exit()

squares = {x**2 for x in range(1,int(n**0.5)+1)}

for a in squares:
    if n - a in squares:
        print(2)
        exit(0)
for a in squares:
    for b in squares:
        if n - a - b in squares:
            print(3)
            exit(0)
print(4)

# DP (파이썬으로는 시간초과, pypy3로는 통과)
# if n ** 0.5 % 1 == 0:
#     print(1)
#     exit()

# dp = [0,1]

# for i in range(2,n+1):
#     minV = 4
#     temp = 1
#     while (temp ** 2) <= i:
#         minV = min(minV, dp[i-temp**2])
#         temp += 1
#     dp.append(minV+1)

# print(dp[n])