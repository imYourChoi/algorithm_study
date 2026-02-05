# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(map(len, strs))

        def helper():
            for i in range(n):
                for j in range(len(strs)-1):
                    if strs[j+1][i] != strs[0][i]:
                        return i
            return n

        return strs[0][:helper()]
