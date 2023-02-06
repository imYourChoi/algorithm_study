# https://www.acmicpc.net/problem/17219

import sys
input=sys.stdin.readline
n,m=map(int, input().split())
d = {(v:=input().split())[0]:v[1] for _ in range(n)}
for _ in range(m): print(d[input().rstrip()])