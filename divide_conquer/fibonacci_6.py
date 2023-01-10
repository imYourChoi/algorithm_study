# https://www.acmicpc.net/problem/11444

n = int(input())

def fibonacci(n):
    n1, n2 = 0, 1
    for i in range(n):
        temp = (n1 + n2) % 1000000007
        n1 = n2
        n2 = temp

    return n1 % 1000000007

print(fibonacci(n))