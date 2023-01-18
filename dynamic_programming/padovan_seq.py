# https://www.acmicpc.net/problem/9461

arr = [1,1,1] + [0 for _ in range(97)]

for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        if arr[i]:
            continue
        arr[i] = arr[i-2] + arr[i-3]
    print(arr[n-1])