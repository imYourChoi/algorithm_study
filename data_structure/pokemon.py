# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline
n,m=map(int,input().split())
d = {}
for i in range(n):
    name = input().rstrip()
    d[str(i+1)] = name
    d[name] = i+1

for i in range(m):
    print(d[input().rstrip()])