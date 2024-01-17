# https://www.acmicpc.net/problem/1038

from itertools import combinations

N = int(input())

answer = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        answer.append(int("".join(map(str, num))))

answer.sort()
if N >= len(answer):
    print(-1)
else:
    print(answer[N])
