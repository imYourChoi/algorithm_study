# https://leetcode.com/problems/container-with-most-water/description/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        answer = 0

        while left < right:
            answer = max(answer, (right - left) *
                         min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return answer
