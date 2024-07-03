# https://www.acmicpc.net/problem/1253

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

count = 0

for i in range(N):
    target = arr[i]
    start = 0
    end = len(arr) - 1

    while start < end:
        sum = arr[start] + arr[end]
        if sum == target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                count += 1
                break
        elif sum > target:
            end -= 1
        elif sum < target:
            start += 1

print(count)
