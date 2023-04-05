# https://www.acmicpc.net/problem/7785

import sys
input = sys.stdin.readline

set = set()
for _ in range(int(input())):
    name, status = input().split()
    if status == "enter":
        set.add(name)
    else:
        set.remove(name)

print(*sorted(list(set), reverse=True), sep="\n")