# https://www.acmicpc.net/problem/10250

n = int(input())

for _ in range(n):
    H, W, N = map(int, input().split())
    print(str(N%H if N%H else H)+str(N//H + 1 if N%H else N//H).zfill(2))