# https://www.acmicpc.net/problem/17608

import sys
input = sys.stdin.readline

rods = [int(input()) for _ in range(int(input()))]
stack = [rods[0]]
answer = 0

for rod in rods:
    while stack and stack[-1] <= rod:
        stack.pop()
    stack.append(rod)

print(len(stack))