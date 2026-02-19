# https://leetcode.com/problems/house-robber/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        two = one = 0

        for num in nums:
            temp = max(one, two + num)
            two = one
            one = temp

        return one
