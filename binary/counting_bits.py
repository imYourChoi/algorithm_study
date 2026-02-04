# https://leetcode.com/problems/counting-bits/description/

from typing import List


def checkSquare(x):
    # if x <= 1:
    #     return False
    # while x % 2 == 0:
    #     x //= 2
    # return x == 1

    if x > 1 and (x & (x - 1) == 0):
        return True
    return False


class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter

        # if n == 0: return [0]
        # if n == 1: return [0,1]

        # dp = [0 for _ in range(n+1)]
        # dp[1] = 1

        # squ = None
        # for i in range(2, n+1):
        #     if checkSquare(i):
        #         dp[i] = 1
        #         squ = i
        #         continue

        #     rem = i - squ
        #     dp[i] = dp[squ] + dp[rem]

        # return dp
