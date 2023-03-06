# https://www.acmicpc.net/problem/14725

import sys
input = sys.stdin.readline

N = int(input())
tunnel = {}

for _ in range(N):
    K, *foods = input().split()
    current = tunnel
    for food in foods:
        if food in current:
            current = current[food]
        else:
            current[food] = {}
            current = current[food]

def printRec(tunnel, level):
    for key in sorted(tunnel.keys()):
        print("-"*level*2 + f"{key}")
        printRec(tunnel[key], level+1)

printRec(tunnel, 0)