# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]

answer = 0
added = 0

for val in reversed(values):
    if added == k:
        continue

    numberCoin = (k - added) // val
    added += numberCoin * val
    answer += numberCoin

print(answer)
