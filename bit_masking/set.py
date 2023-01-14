# https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline

n = int(input())
store = 0
for _ in range(n):
    op = input().rstrip()
    
    if op == "all":
        store = 2 ** 20-1
        continue
    elif op == "empty":
        store = 0
        continue
    op, num = op.split()
    num = int(num)
    if op == "add":
        store = store | (2 ** (num - 1))
    elif op == "remove":
        store = store & ((2 ** 20 - 1) ^ (2 ** (num - 1)))
    elif op == "check":
        if store & (2 ** (num - 1)):
            print(1)
        else: print(0)
    elif op == "toggle":
        store = store ^ (2 ** (num - 1))