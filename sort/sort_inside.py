# https://www.acmicpc.net/problem/1427

from collections import Counter

c = Counter(input())
for n in sorted(c, reverse=True):
    print(str(n)*c[n], end="")
print()