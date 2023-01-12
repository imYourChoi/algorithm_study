# https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())
array = [x for x in range(1, N+1)]
answer = []

num = 0
while array:
    num += K-1
    if num >= len(array):
        num = num%len(array)
    answer.append(str(array.pop(num)))
print("<"+", ".join(answer)+">")