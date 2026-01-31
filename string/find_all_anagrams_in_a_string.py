# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        pCounter = Counter(p)

        limit = len(s) - len(p)
        answer = []

        for i in range(len(p)):
            if s[i] in pCounter:
                pCounter[s[i]] -= 1

        flag = all(val == 0 for val in pCounter.values())

        for i in range(limit):
            if flag:
                answer.append(i)
                if s[i] != s[i+len(p)]:
                    flag = False
                    pCounter[s[i]] += 1
                    if s[i+len(p)] in pCounter:
                        pCounter[s[i+len(p)]] -= 1
            else:
                if s[i] in pCounter:
                    pCounter[s[i]] += 1
                if s[i+len(p)] in pCounter:
                    pCounter[s[i+len(p)]] -= 1
                flag = all(val == 0 for val in pCounter.values())

        if flag:
            answer.append(limit)

        return answer
