# https://www.acmicpc.net/problem/10872

n = int(input())

def factorial(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    return num * factorial(num - 1)
    
print(factorial(n))