# https://leetcode.com/problems/next-permutation/description/

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = -1

        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                start = i-1
                break

        if start == -1:
            for i in range(n//2):
                nums[i], nums[n-1-i] = nums[n-1-i], nums[i]
            return

        larger = n - 1

        for i in range(n-1, start, -1):
            if nums[i] > nums[start]:
                larger = i
                break

        nums[start], nums[larger] = nums[larger], nums[start]

        for i in range(start + 1, (start+n)//2+1):
            opp = n - 1 - (i - (start + 1))
            nums[i], nums[opp] = nums[opp], nums[i]
