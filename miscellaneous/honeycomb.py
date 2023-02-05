# https://www.acmicpc.net/problem/2292

n = int(input())
answer = 1
temp = 1
while True:
    if temp >= n:
        print(answer)
        break
    temp += answer * 6
    answer += 1