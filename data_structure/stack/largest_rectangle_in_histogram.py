# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        answer = 0

        for i in range(len(heights)):
            height = heights[i]
            count = 0
            lastI, lastH = 0, 0
            while stack and stack[-1][1] >= height:
                count += 1
                lastI, lastH = stack.pop()
                answer = max(answer, lastH * (i - lastI))

            if count > 0:
                stack.append((lastI, height))
            else:
                stack.append((i, height))

        while stack:
            lastI, lastH = stack.pop()
            answer = max(answer, lastH * (len(heights) - lastI))

        return answer
