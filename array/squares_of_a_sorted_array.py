# https://leetcode.com/problems/squares-of-a-sorted-array/description/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >= 0:
            return list(map(lambda x: x ** 2, nums))
        if nums[-1] <= 0:
            return list(map(lambda x: x ** 2, reversed(nums)))

        n = len(nums)
        left, right = 0, n - 1

        result = [0] * n
        count = n - 1

        while left <= right:
            if -nums[left] < nums[right]:
                result[count] = (nums[right] ** 2)
                right -= 1
            else:
                result[count] = (nums[left] ** 2)
                left += 1
            count -= 1

        return result
