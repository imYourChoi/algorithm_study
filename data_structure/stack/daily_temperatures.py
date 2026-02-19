# https://leetcode.com/problems/daily-temperatures/description/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
                continue

            while stack and stack[-1][1] < temp:
                lastI, lastT = stack.pop()

                result[lastI] = i - lastI

            stack.append((i, temp))

        return result
