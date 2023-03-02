# https://www.acmicpc.net/problem/9252

a,b = input(), input()

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
dp_pos = [[None] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i ==0 or j == 0:
            dp[i][j] = 0
        elif a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            dp_pos[i][j] = (i-1, j-1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            I,J = max((i-1,j), (i,j-1), key=lambda x: dp[x[0]][x[1]])
            dp_pos[i][j] = dp_pos[I][J]

if not dp_pos[-1][-1]:
    print(dp[-1][-1])
else:
    i,j = dp_pos[-1][-1]
    answer = ""
    while dp_pos[i][j]:
        answer = a[i] + answer
        i,j = dp_pos[i][j]
    answer = a[i] + answer
    print(dp[-1][-1])
    print(answer)