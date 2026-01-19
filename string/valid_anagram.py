# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = {}

        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if c not in d or d[c] == 0:
                return False
            d[c] -= 1

        return True
