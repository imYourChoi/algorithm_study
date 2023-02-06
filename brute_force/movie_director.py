# https://www.acmicpc.net/problem/1436

n = int(input())
answer = 0
temp = 666
while True:
    if "666" in str(temp):
        answer += 1
    if answer == n:
        print(temp)
        break
    temp += 1
