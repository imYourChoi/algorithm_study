import sys
import math

t = int(input())
answer = []
for _ in range(t):
    n, *nums = list(map(int, sys.stdin.readline().split()))
    total = 0
    for i in range(n):
        for j in range(i+1, n):
            total += math.gcd(nums[i], nums[j])

    answer.append(total)

print(*answer, sep="\n")
