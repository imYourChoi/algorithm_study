# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = nums[0]

        left = 0
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] >= first:
                left = mid
            else:
                right = mid

        offset = len(nums) - right

        left = -1
        right = len(nums)

        while left + 1 < right:
            mid = (left + right) // 2
            realMid = (mid - offset) % len(nums)

            if nums[realMid] < target:
                left = mid
            elif target < nums[realMid]:
                right = mid
            else:
                return realMid

        return -1
