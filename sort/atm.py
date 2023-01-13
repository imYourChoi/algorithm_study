# https://www.acmicpc.net/problem/11399

input()
answer = 0
temp = 0
for time in sorted(list(map(int, input().split()))):
    temp += time
    answer += temp
print(answer)