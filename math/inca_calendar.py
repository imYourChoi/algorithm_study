# https://www.acmicpc.net/problem/6064
# https://www.acmicpc.net/board/view/21503

import sys
input = sys.stdin.readline

def gcd(a,b):
    Q = a // b
    R = a % b
    if R == 0:
        return b
    else: return gcd(b, R)

for i in range(int(input())):
    m,n,x,y = map(int,input().split())
    lcm = m*n//gcd(m,n)
    temp = x
    answer = 0
    while temp <= lcm:
        if temp % n == y % n:
            answer = temp
            break
        temp += m
    # for item in arr:
    #     if item % n == y % n:
    #         answer = item
    #         break
    # arr = []
    # temp = x
    # while temp <= lcm:
    #     arr.append(temp)
    #     temp += m
    # answer = 0
    # for item in arr:
    #     if item % n == y % n:
    #         answer = item
    #         break
    if answer:
        print(answer)
    else:
        print(-1)