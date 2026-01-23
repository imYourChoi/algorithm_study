# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if stack and paren[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack
