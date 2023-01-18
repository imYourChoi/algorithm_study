# https://www.acmicpc.net/problem/9184

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

arr = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def function(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return function(20,20,20)
    if arr[a][b][c]:
        return arr[a][b][c]
    if a < b < c:
        arr[a][b][c] = function(a, b, c-1) + function(a, b-1, c-1) - function(a, b-1, c)
        return arr[a][b][c]
    arr[a][b][c] = function(a-1, b, c) + function(a-1, b-1, c) + function(a-1, b, c-1) - function(a-1, b-1, c-1)
    return arr[a][b][c]

while True:
    a,b,c = map(int, input().split())
    if a==b==c==-1:
        break
    print("w(%d, %d, %d) = %d"  % (a,b,c,function(a,b,c)))