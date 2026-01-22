# https://leetcode.com/problems/ransom-note/description/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterM = Counter(magazine)
        counterR = Counter(ransomNote)

        return counterM & counterR == counterR
