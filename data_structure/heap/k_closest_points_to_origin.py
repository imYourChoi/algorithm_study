# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            x, y = point
            dist = x ** 2 + y ** 2
            heapq.heappush(pq, (dist, point))

        answer = []
        for i in range(k):
            answer.append(heapq.heappop(pq)[1])

        return answer
