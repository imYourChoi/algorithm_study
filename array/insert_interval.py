# https://leetcode.com/problems/insert-interval/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []

        newS, newE = newInterval

        for i in range(len(intervals)):
            curS, curE = intervals[i]
            if curE < newInterval[0]:
                left.append([curS, curE])
            elif newInterval[1] < curS:
                right.append([curS, curE])
            else:
                newS = min(newS, curS)
                newE = max(newE, curE)

        return left + [[newS, newE]] + right
