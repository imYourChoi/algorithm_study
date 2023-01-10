# https://www.acmicpc.net/problem/1300

N, k = int(input()), int(input())
start, end = 1, k
answer = 0

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, N + 1):
        temp += min(mid // i, N)
    
    if temp >= k:
        answer = mid
        end = mid -1
    else:
        start = mid + 1

print(answer)