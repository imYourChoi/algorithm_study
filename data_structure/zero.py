# https://www.acmicpc.net/problem/10773

import sys
input=sys.stdin.readline
stack = []
for _ in range(int(input())):
    n = input().rstrip()
    if n == "0":
        stack.pop()
    else:
        stack.append(int(n))
print(sum(stack))