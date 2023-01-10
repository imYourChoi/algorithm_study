# https://www.acmicpc.net/problem/1629

import sys
import math
a, b, c = list(map(int, sys.stdin.readline().rstrip().split(" ")))

def multiply(a, b, c):
    if b == 1:
        return a % c
    temp = multiply(a, b // 2, c)
    if b % 2 == 1:
        return temp ** 2 * a % c
    return temp ** 2 % c

num = multiply(a, b, c) 
print(num)