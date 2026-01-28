# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        i = 0
        digits = []
        sign = 1
        if s[0] in ["+", "-"]:
            if s[0] == "-":
                sign *= -1
            i += 1

        while i < len(s) and s[i].isdecimal():
            if digits or s[i] != "0":
                digits.append(s[i])
            i += 1

        print(digits)

        if not digits:
            return 0

        answer = int("".join(digits))
        # for i, digit in enumerate(digits):
        #     answer += 10 ** (len(digits) - i - 1) * digits[i]

        answer *= sign

        return max(-2 ** 31, min(answer, 2 ** 31 - 1))
