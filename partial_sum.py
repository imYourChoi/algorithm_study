# https://www.acmicpc.net/problem/1806

N,S = map(int,input().split())
array = list(map(int, input().split()))

total = array[0]
start, end = 0,0
answer = N + 1

while start < N:
    if end == N-1:
        if total >= S:
            answer = min(answer, end - start + 1)
        total -= array[start]
        start += 1
    elif total >= S:
        answer = min(answer, end - start + 1)
        total -= array[start]
        start += 1
        if start > end:
            end += 1
    else:
        end += 1
        total += array[end]

if answer == N + 1:
    print(0)
else:
    print(answer)