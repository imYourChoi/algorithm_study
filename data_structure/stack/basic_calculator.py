# https://leetcode.com/problems/basic-calculator/description/

class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v, stack):
            if op == "+":
                stack.append(v)
            elif op == "-":
                stack.append(-v)

        i = 0
        num = 0
        currentStack = []
        metaStack = []
        sign = "+"

        while i < len(s):
            c = s[i]

            if c.isdecimal():
                num = num * 10 + int(c)

            elif c in "+-":
                update(sign, num, currentStack)
                num = 0
                sign = c

            elif c == "(":
                metaStack.append((currentStack, sign))

                currentStack = []
                num = 0
                sign = "+"

            elif c == ")":
                update(sign, num, currentStack)

                num = sum(currentStack)
                currentStack, sign = metaStack.pop()

            i += 1

        update(sign, num, currentStack)

        return sum(currentStack)
