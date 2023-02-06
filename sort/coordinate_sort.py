# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline
arr = [tuple(map(int, input().rstrip().split())) for _ in range(int(input()))]

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

for a,b in arr:
    print(a,b)