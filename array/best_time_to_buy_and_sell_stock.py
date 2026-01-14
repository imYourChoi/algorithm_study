# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 10101
        maxi = -1
        answer = 0

        for i in range(len(prices)):
            price = prices[i]
            if mini > price:
                mini = price
                maxi = -1
            if maxi < price:
                maxi = price
                if maxi - mini > answer:
                    answer = maxi - mini

        return answer
