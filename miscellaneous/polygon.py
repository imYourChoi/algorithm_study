# https://www.acmicpc.net/problem/2166

import sys
input = sys.stdin.readline
n = int(input())
coord = [tuple(map(int, input().split())) for _ in range(n)]

area = 0
for i in range(n):
    area += (coord[i][0]+coord[i-1][0]) * (coord[i][1]-coord[i-1][1])

print(abs(area/2))