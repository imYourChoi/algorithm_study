# https://www.acmicpc.net/problem/1213

from collections import Counter
counter = Counter(input())
if list(map(lambda x: x%2,counter.values())).count(1) > 1:
    print("I'm Sorry Hansoo")
else:
    mid = ""
    s = ""
    for a,c in (l:=sorted(counter.items())):
        if c % 2:
            mid = a
        s += a*(c//2)
    s = s + mid + s[::-1]
    print(s)