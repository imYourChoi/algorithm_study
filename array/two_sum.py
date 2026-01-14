# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashMap:
                return [i, hashMap[compliment]]
            hashMap[nums[i]] = i
        return []
