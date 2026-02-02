# https://leetcode.com/problems/word-ladder/description/

from collections import deque, defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        graph = defaultdict(set)

        wordSet = set(wordList)

        for word in wordSet:
            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                placeholder = left + "_" + right

                graph[placeholder].add(word)

        queue = deque([(beginWord, 1)])
        while queue:
            word, num = queue.popleft()

            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                placeholder = left + "_" + right

                for neighbor in graph[placeholder]:
                    if neighbor == endWord:
                        return num + 1

                    if neighbor not in wordSet:
                        continue
                    wordSet.remove(neighbor)

                    queue.append((neighbor, num + 1))

        return 0
