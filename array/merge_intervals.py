# https://leetcode.com/problems/merge-intervals/description/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        answer = []
        curS, curE = intervals[0]

        for start, end in intervals[1:]:
            if start <= curE:
                curE = max(end, curE)
            else:
                answer.append([curS, curE])
                curS = start
                curE = end

        answer.append([curS, curE])
        return answer
