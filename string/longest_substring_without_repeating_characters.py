# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        index = {}
        answer = 0

        for right in range(len(s)):
            if s[right] not in index or index[s[right]] < left:
                index[s[right]] = right
                answer = max(answer, right - left + 1)
            else:
                left = index[s[right]] + 1
                index[s[right]] = right

        return answer
