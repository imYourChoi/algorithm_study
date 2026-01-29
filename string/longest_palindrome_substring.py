# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palin = [set([1]) for _ in range(n)]

        start = 0
        palinLen = 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palin[i].add(2)
                start = i
                palinLen = 2

        for i in range(3, n + 1):
            for j in range(n - i + 1):
                if s[j] == s[j + i - 1] and (i - 2 in palin[j + 1]):
                    palin[j].add(i)
                    if i > palinLen:
                        start = j
                        palinLen = i

        return s[start: start + palinLen]
