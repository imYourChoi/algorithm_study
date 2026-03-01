# https://leetcode.com/problems/top-k-frequent-words/description/

from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = defaultdict(int)

        for word in words:
            hashMap[word] += 1

        pq = []

        for word, value in hashMap.items():
            heapq.heappush(pq, (-value, word))

        result = [heapq.heappop(pq)[1] for _ in range(k)]

        return result
