# https://www.acmicpc.net/problem/4673

s = set([x for x in range(1,10001)])

for i in range(1,10001):
    s.discard(i+sum(map(int, [*str(i)])))
for i in s:
    print(i)