# https://leetcode.com/problems/palindrome-number/description/

from math import log10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = int(log10(x)) + 1 if x else 0

        for i in range(n // 2):
            comp = n - i - 1

            left = (x // (10 ** comp)) % 10
            right = (x // (10 ** i)) % 10
            if left != right:
                return False

        return True
