# https://www.acmicpc.net/problem/1094

n = int(input())
answer = 0

while n > 0:
    temp = 1
    while temp * 2 <= 64 and temp * 2 <= n:
        temp *= 2
    n -= temp
    answer += 1

print(answer)

# print(int(input()).bit_count())