# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        answer = []

        def backtrack(cur, i):
            if i == len(digits):
                answer.append("".join(cur))

                return

            for c in mapping[digits[i]]:
                cur.append(c)
                backtrack(cur, i + 1)
                cur.pop()

        backtrack([], 0)

        return answer
