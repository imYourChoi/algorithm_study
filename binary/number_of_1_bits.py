# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n > 0:
            answer += n % 2
            n >>= 1

        return answer
