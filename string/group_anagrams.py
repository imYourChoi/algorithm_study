# https://leetcode.com/problems/group-anagrams/description/

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS in dictionary:
                dictionary[sortedS].append(s)
            else:
                dictionary[sortedS] = [s]

        return list(dictionary.values())
