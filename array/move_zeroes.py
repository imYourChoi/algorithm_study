# https://leetcode.com/problems/move-zeroes/description/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        non = 0

        for i in range(n):
            if nums[i] != 0 or non == n:
                non = max(i+1, non)
                continue

            while non < n and nums[non] == 0:
                non += 1

            if i < non < n:
                nums[i], nums[non] = nums[non], nums[i]
