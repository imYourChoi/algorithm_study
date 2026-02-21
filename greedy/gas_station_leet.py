# https://leetcode.com/problems/gas-station/description/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        totalSurplus = 0
        surplus = 0
        start = 0

        for i in range(n):
            cur = gas[i] - cost[i]
            totalSurplus += cur
            surplus += cur
            if surplus < 0:
                surplus = 0
                start = i + 1

        return -1 if totalSurplus < 0 else start
