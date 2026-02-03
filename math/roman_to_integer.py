# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        answer = 0
        for i, c in enumerate(s):
            if i + 1 < len(s) and table[s[i+1]] > table[s[i]]:
                answer -= table[s[i]]
            else:
                answer += table[s[i]]

        return answer
