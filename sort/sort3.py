# https://www.acmicpc.net/problem/10989

import sys

n = int(sys.stdin.readline())
array = []
d= {}

for _ in range(n):
    num = int(sys.stdin.readline())
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
        array.append(num)

for num in sorted(array):
    for _ in range(d[num]):
        print(num)