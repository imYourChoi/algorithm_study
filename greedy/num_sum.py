# https://www.acmicpc.net/problem/1789
n = int(input())
temp, answer = 0, 0
while temp <= n:
    answer += 1
    temp += answer
print(answer-1)