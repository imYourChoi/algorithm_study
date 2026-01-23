# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        cur = nums[0]

        for num in nums[1:]:
            cur += num
            cur = max(num, cur)
            answer = max(answer, cur)

        return answer
