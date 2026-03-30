# https://leetcode.com/problems/rotate-array/description/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        for i, n in enumerate(nums[-k:] + nums[:-k]):
            nums[i] = n
