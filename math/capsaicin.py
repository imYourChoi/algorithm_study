# https://www.acmicpc.net/problem/15824

n = int(input())
array = sorted(list(map(int, input().split())))

div = 1000000007
answer = 0

def pow(num, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return num
    half = pow(num, exp // 2)
    if exp % 2:
        return half * half * num % div
    return half * half % div

for i in range(n):
    answer += array[i] * (pow(2,i) - pow(2, n-i-1))

print(answer % div)