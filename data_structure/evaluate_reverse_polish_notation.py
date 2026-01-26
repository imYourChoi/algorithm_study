# https://leetcode.com/problems/evaluate-reverse-polish-notation/


from typing import List


def isNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if isNumber(token):
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(int(left / right))

        return stack[0]
