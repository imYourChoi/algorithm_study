# https://leetcode.com/problems/maximum-product-subarray/description/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = cMax = cMin = nums[0]

        for num in nums[1:]:
            if num < 0:
                cMax, cMin = cMin, cMax

            cMax = max(num, cMax * num)
            cMin = min(num, cMin * num)

            answer = max(cMax, answer)

        return answer
