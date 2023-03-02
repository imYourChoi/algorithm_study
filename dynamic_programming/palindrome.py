# https://www.acmicpc.net/problem/10942

import sys
input = sys.stdin.readline

N = int(input())
numbers = [0] + list(map(int, input().split()))
M = int(input())
dp = [[False] * (N+1) for _ in range(N+1)]
# dp = [[None] * (N+1) for _ in range(N+1)]
answer = []

def palindrome(S,E):
    start, end = S,E
    while S < E:
        if dp[S][E]:
            for i in range(start, S+1):
                dp[i][end-(i-start)] = True
            return 1
        # elif dp[S][E] == False:
        #     for i in range(start, S+1):
        #         dp[i][end-(i-start)] = False
        #     return 0
        if numbers[S] == numbers[E]:
            S += 1
            E -= 1
        else:
            # for i in range(start, S+1):
            #     dp[i][end-(i-start)] = False
            return 0
    for i in range(start, (start+end)//2+1):
        dp[i][end-(i-start)] = True
    return 1
for _ in range(M):
    S,E = map(int, input().split())
    answer.append(palindrome(S,E))
print(*answer, sep="\n")
# print(*dp, sep="\n")