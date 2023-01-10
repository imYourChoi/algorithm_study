# https://www.acmicpc.net/problem/11401

N, K = list(map(int, input().split()))

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num = i * num % 1000000007
    return num

def multiply(a, b):
    if b == 1:
        return a % 1000000007
    temp = multiply(a, b // 2)
    if b % 2 == 1:
        return temp ** 2 * a % 1000000007
    return temp ** 2 % 1000000007

divisor = (factorial(N-K) * factorial(K)) % 1000000007
answer = factorial(N) * multiply(divisor, 1000000007 - 2) % 1000000007
print(answer)