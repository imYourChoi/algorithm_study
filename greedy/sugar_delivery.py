# https://www.acmicpc.net/problem/2839

n = int(input())
answer = 0
while n:
    if not n%5:
        print(n//5+answer)
        exit(0)
    n -= 3
    answer += 1
    if n < 0:
        print(-1)
        exit(0)
print(answer)