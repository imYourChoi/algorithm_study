# https://leetcode.com/problems/unique-paths/description/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[0][1] = 1

        for y in range(1, m+1):
            for x in range(1, n+1):
                dp[y][x] = dp[y-1][x] + dp[y][x-1]

        return dp[m][n]
