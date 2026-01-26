# https://leetcode.com/problems/word-break/

from typing import List


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur:
                cur[c] = {}

            cur = cur[c]

        cur["*"] = ''

    def search(self, word):
        cur = self.root

        matches = []

        for i in range(len(word)):
            c = word[i]
            if c not in cur:
                break

            cur = cur[c]
            if "*" in cur:
                matches.append(i+1)

        return matches


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue

            matches = trie.search(s[i:])

            for match in matches:
                dp[i + match] = True

        return dp[-1]
