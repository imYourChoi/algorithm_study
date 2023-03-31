# https://www.acmicpc.net/problem/17404

import sys
input = sys.stdin.readline
inf = float('inf')

array = []
for i in range(n:=int(input())):
    r,g,b = map(int, input().split())
    if not array:
        array = [[r, inf, inf], [inf, g, inf], [inf, inf, b]]
        continue
    temp = []
    for each in array:
        tr = min(each[1], each[2]) + r
        tg = min(each[0], each[2]) + g
        tb = min(each[0], each[1]) + b
        temp.append([tr, tg, tb])
    array = temp

print(min(*array[0][1:3], array[1][0], array[1][2], *array[2][0:2]))