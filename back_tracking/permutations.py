# https://leetcode.com/problems/permutations/description/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(cur, remain, answer):
            if not remain:
                return answer.append(cur)

            for i in range(len(remain)):
                helper(cur + [remain[i]], remain[:i] + remain[i+1:], answer)

            return answer

        return helper([], nums, [])
