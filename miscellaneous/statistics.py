# https://www.acmicpc.net/problem/2108

import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(int(input()))]
modeList = [0] * 8001
for num in nums:
    modeList[num+4000] += 1
value = max(modeList)
mode = modeList.index(value)
if modeList.count(value) > 1:
    mode = modeList.index(value, mode+1)
mode -= 4000
print(round(sum(nums)/len(nums)))
print(sorted(nums)[(len(nums)-1)//2])
print(mode)
print(max(nums) - min(nums))