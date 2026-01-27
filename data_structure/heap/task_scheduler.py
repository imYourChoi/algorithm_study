# https://leetcode.com/problems/task-scheduler/description/

import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = []
        counter = Counter(tasks)

        for key, freq in counter.items():
            heapq.heappush(pq, (-freq, key))

        answer = 0

        while pq:
            temp = []
            cycle = n + 1

            while cycle and pq:
                freq, key = heapq.heappop(pq)
                freq = -freq

                if freq > 1:
                    temp.append((-(freq-1), key))

                cycle -= 1
                answer += 1

            for task in temp:
                heapq.heappush(pq, task)

            if not pq:
                break
            else:
                answer += cycle

        return answer
