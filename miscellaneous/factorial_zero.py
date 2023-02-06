# https://www.acmicpc.net/problem/1676

n = int(input())
num = 1
for i in range(n): num *= (i+1)
print(len(str(num))-len(str(int(str(num)[::-1]))))