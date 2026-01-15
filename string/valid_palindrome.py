# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(c for c in s if c.isalnum()).lower()

        for i in range(len(clean_s) // 2):
            if clean_s[i] != clean_s[len(clean_s) - 1 - i]:
                return False
        return True
