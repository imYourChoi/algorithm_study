# https://www.acmicpc.net/problem/11659

import sys
input=sys.stdin.readline
from itertools import accumulate

n,m = map(int,input().split())
nums = list(accumulate((map(int, input().split()))))

for _ in range(m):
    i,j = map(int, input().split())
    if i == 1:
        print(nums[j-1])
    else:
        print(nums[j-1] - nums[i-2])