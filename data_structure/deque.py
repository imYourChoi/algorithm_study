# https://www.acmicpc.net/problem/10866

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stack = deque([])
for _ in range(n):
    command = input().split()
    if command[0] == "push_front":
        stack.appendleft(command[1])
    if command[0] == "push_back":
        stack.append(command[1])
    if command[0] == "pop_front":
        if not stack:
            print(-1)
        else:
            print(stack.popleft())
    if command[0] == "pop_back":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    if command[0] == "size":
        print(len(stack))
    if command[0] == "empty":
        print(0 if len(stack) else 1)
    if command[0] == "front":
        if not stack:
            print(-1)
        else:
            print(stack[0])
    if command[0] == "back":
        if not stack:
            print(-1)
        else:
            print(stack[-1])