# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline
n = int(input())
array = [list(map(int, input().rstrip().split())) for _ in range(n)]

array.sort(key=lambda x:x[0])
array.sort(key=lambda x:x[1])

end = 0
count = 0
for meeting in array:
    if meeting[0] >= end:
        end = meeting[1]
        count += 1

print(count)