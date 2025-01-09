# https://www.acmicpc.net/problem/2343

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

start = max(lessons)
end = sum(lessons)

while start <= end:
    mid = (start + end) // 2

    count = 1
    total = 0
    for time in lessons:
        if total + time > mid:
            count += 1
            total = 0
        total += time

    if count <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
