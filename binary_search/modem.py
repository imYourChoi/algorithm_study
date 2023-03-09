# https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

N,C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])
answer = 0
start, end = 0, house[-1] - house[0]

if C == 2:
    print(house[-1] - house[0])
else:
    while start < end:
        mid = (start + end) // 2

        count = 1
        last = house[0]

        for i in range(N):
            if house[i] - last >= mid:
                count += 1
                last = house[i]
        if count >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid
    print(answer)