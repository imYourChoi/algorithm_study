# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

array = []
for i in range(int(input())):
    r,g,b = map(int, input().split())
    if not array:
        array = [r,g,b]
        continue
    tr = min(array[1], array[2]) + r
    tg = min(array[0], array[2]) + g
    tb = min(array[0], array[1]) + b
    array = [tr, tg, tb]

print(min(array))