# https://www.acmicpc.net/problem/2751

import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

for num in sorted(array):
    print(num)