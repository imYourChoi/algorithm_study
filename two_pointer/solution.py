# https://www.acmicpc.net/problem/2467

n = int(input())
solutions = list(map(int, input().split()))

start, end = 0, n-1
combined = float('inf')
answer = (None, None)

while start < end:
    if abs(add := solutions[start] + solutions[end]) < abs(combined):
        combined = abs(solutions[start] + solutions[end])
        answer = (solutions[start], solutions[end])
    elif add <= 0:
        start += 1
    elif add > 0:
        end -= 1

print(*answer)