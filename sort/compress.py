# https://www.acmicpc.net/problem/18870

n = int(input())
ori = list(map(int, input().split()))
array = sorted(set(ori))
d = {}
for idx, val in enumerate(array):
    d[val] = idx

for item in ori:
    print(d[item], end=" ")
print()