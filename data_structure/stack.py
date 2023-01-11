# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.append(command[1])
    if command[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    if command[0] == "size":
        print(len(stack))
    if command[0] == "empty":
        print(0 if len(stack) else 1)
    if command[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])