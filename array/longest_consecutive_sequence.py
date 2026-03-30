# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        answer = 0
        for num in numSet:
            if num - 1 not in numSet:
                consecutive = num + 1
                while consecutive in numSet:
                    consecutive += 1
                answer = max(answer, consecutive - num)

        return answer
