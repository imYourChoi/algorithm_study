# https://leetcode.com/problems/longest-palindrome/description/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        answer = 0
        odd = False
        for element, count in counter.items():
            if not odd and count % 2 == 1:
                odd = True
            answer += count - (count % 2)

        return answer + odd
