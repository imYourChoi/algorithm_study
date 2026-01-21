# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]

        n = len(nums)

        acc = 1
        for i in range(n):
            answer[i] *= acc
            acc *= nums[i]

        acc = 1
        for i in range(n-1, -1, -1):
            answer[i] *= acc
            acc *= nums[i]

        return answer
