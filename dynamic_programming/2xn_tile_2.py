# https://www.acmicpc.net/problem/11727

n = int(input())

array = [0, 1, 3]

for i in range(3, n+1):
    array.append(array[i-1] + array[i-2]*2)

print(array[n] % 10007)