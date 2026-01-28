# https://leetcode.com/problems/trapping-rain-water/description/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        answer = 0

        lMax = height[0]

        for h in height:
            if not stack or stack[-1] > h:
                stack.append(h)
                continue

            if lMax > h:
                last = None
                i = -1
                while stack and stack[i] < h:
                    answer += h - stack[i]
                    stack[i] = h
                    i -= 1
            else:
                while stack:
                    answer += lMax - stack.pop()
                lMax = h

            stack.append(h)

        return answer
