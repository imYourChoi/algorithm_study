# https://www.acmicpc.net/problem/2775

for _ in range(int(input())):
    k,n = int(input()), int(input())
    array = [x for x in range(1,n+1)]
    for i in range(k):
        for j in range (n-1):
            array[j+1] += array[j]
    print(array[-1])