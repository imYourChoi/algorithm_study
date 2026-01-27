# https://leetcode.com/problems/maximum-containers-on-a-ship/description/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        total = total // 2
        dp = [False for _ in range(total+1)]
        dp[0] = True

        for num in nums:
            for i in range(total, num-1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[-1]
