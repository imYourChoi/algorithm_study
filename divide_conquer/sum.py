# https://www.acmicpc.net/problem/13172

import sys, math
input = sys.stdin.readline

X = 1000000007
n = int(input())
answer = 0

def equation(N,S):
    return S * multiply(N, X-2) % X

def multiply(num, exp):
    if exp == 1:
        return num
    half = multiply(num, exp // 2)
    if exp % 2 == 0:
        return half * half % X
    else:
        return num * half * half % X

for _ in range(n):
    N,S = map(int, input().split())
    gcd = math.gcd(N,S)
    N //= gcd
    S //= gcd
    answer += equation(N,S)

print(answer%X)