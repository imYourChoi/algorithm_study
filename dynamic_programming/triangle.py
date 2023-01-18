# https://www.acmicpc.net/problem/1932

n = int(input())
arr = [[0]] + [[0] + list(map(int, input().split())) for _ in range(n)]

for i in range(2,n+1):
    for j in range(1,i+1):
        if j == 1:
            arr[i][j] += arr[i-1][j]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i-1][j], arr[i-1][j-1]) + arr[i][j]

print(max(arr[-1]))
# for row in arr:
#     print(row)
