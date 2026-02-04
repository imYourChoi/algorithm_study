# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 or j >= 0:
            skip_s = 0
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            skip_t = 0
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            if (i >= 0) != (j >= 0):
                return False

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True

        ################

        # si, ti = len(s) - 1, len(t) - 1
        # sc, tc = 0, 0

        # while si >= 0 and ti >= 0:
        #     if s[si] != "#" and t[ti] != "#":
        #         if s[si] != t[ti]:
        #             return False
        #         si -= 1
        #         ti -= 1
        #         continue

        #     while si >= 0 and (s[si] == "#" or sc > 0):
        #         if s[si] == "#": sc += 1
        #         else: sc -= 1
        #         si -= 1

        #     while ti >= 0 and (t[ti] == "#" or tc > 0):
        #         if t[ti] == "#": tc += 1
        #         else: tc -= 1
        #         ti -= 1

        # while si >= 0 and (s[si] == "#" or sc > 0):
        #     if s[si] == "#": sc += 1
        #     else: sc -= 1
        #     if sc < 0: return False
        #     si -= 1

        # while ti >= 0 and (t[ti] == "#" or tc > 0):
        #     if t[ti] == "#": tc += 1
        #     else: tc -= 1
        #     if tc < 0: return False
        #     ti -= 1

        # return si == -1 and ti == -1

        ################

        # stack = []

        # for c in s:
        #     if c == "#":
        #         if stack: stack.pop()
        #     else:
        #         stack.append(c)
        # sRes = "".join(stack)

        # stack = []
        # for c in t:
        #     if c == "#":
        #         if stack: stack.pop()
        #     else:
        #         stack.append(c)
        # tRes = "".join(stack)

        # return sRes == tRes
