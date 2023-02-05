# https://www.acmicpc.net/problem/2231

n=int(input())
answer = 0
for i in range(n):
    if sum(map(int,[*str(i)]))+i == n:
        answer = i
        break
print(answer)