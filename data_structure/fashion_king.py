# https://www.acmicpc.net/problem/9375

import sys, math
input = sys.stdin.readline

for _ in range(int(input())):
    d = dict()
    for _ in range(int(input())):
        name, kind = input().split()
        if kind in d:
            d[kind] += 1
        else: d[kind] = 2
    
    print(math.prod(d.values()) - 1)