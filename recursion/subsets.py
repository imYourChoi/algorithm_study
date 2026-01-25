# https://leetcode.com/problems/subsets/

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        temp = []

        def helper(index):
            answer.append(temp[:])

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                temp.append(nums[i])
                helper(i + 1)
                temp.pop()

        helper(0)

        return answer
