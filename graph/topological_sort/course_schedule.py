# https://leetcode.com/problems/course-schedule/description/

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0 for _ in range(numCourses)]
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            inDegree[a] += 1
            graph[b].append(a)

        queue = deque()

        remaining = numCourses

        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                remaining -= 1

        while queue:
            current = queue.popleft()
            for node in graph[current]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    queue.append(node)
                    remaining -= 1

        return remaining == 0
