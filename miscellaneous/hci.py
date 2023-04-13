# https://www.acmicpc.net/problem/16139

import sys
input = sys.stdin.readline

s = input().strip()
answer = []
acc = [[0 for i in range(len(s))] for i in range(26)]
set = set()

for _ in range(int(input())):
    alpha, start, end = input().split();
    start, end = int(start), int(end)
    if alpha in set:
        answer.append(acc[ord(alpha) - 97][end] - (acc[ord(alpha) - 97][start - 1] if start else 0))
    else:
        set.add(alpha)
        array = acc[ord(alpha)-97]
        for i, c in enumerate(s):
            if i: array[i] = array[i-1] + (c == alpha)
            else: array[0] = 0 + (c == alpha)
        answer.append(array[end] - (array[start-1] if start else 0))

print(*answer, sep="\n")