# https://leetcode.com/problems/add-binary/description/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        carry = 0

        ai = len(a) - 1
        bi = len(b) - 1

        while ai >= 0 or bi >= 0 or carry:
            if ai >= 0:
                carry += int(a[ai])
                ai -= 1
            if bi >= 0:
                carry += int(b[bi])
                bi -= 1

            answer.append(str(carry % 2))
            carry = carry // 2

        return "".join(reversed(answer))
