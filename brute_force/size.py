# https://www.acmicpc.net/problem/7568

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    v = 1
    for j in range(n):
        if p[j][0] > p[i][0] and p[j][1] > p[i][1]:
            v += 1
    print(v,end=" ")
print()