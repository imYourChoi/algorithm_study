# https://www.acmicpc.net/problem/1449

N,L = map(int,input().split())
locations = sorted(list(map(int, input().split())))
current = 0
answer = 0
for location in locations:
    if location > current:
        current = location - 0.5 + L
        answer += 1
print(answer)