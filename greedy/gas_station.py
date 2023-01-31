# https://www.acmicpc.net/problem/13305

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
tempPrice = 10000000000 # 1e10 같은 실수 자료형은 실수 오차가 발생할 수 있음!!
tempDist = 0

for i in range(n-1):
    if price[i] < tempPrice:
        answer += tempPrice * tempDist
        tempPrice = price[i]
        tempDist = 0
    tempDist += distance[i]
answer += tempPrice * tempDist
print(answer)