# https://www.acmicpc.net/problem/2217

import sys
input = sys.stdin.readline
n = int(input())
ropes = sorted([int(input()) for _ in range(n)], reverse=True)

answer = 0
for idx, rope in enumerate(ropes):
    answer = max(answer, (idx+1) * rope)

print(answer)