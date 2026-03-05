# https://leetcode.com/problems/course-schedule-ii/description/

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder = [0] * numCourses
        visited = [False] * numCourses
        graph = [set() for _ in range(numCourses)]

        for a, b in prerequisites:
            inorder[a] += 1
            graph[b].add(a)

        nodes = [i for i, x in enumerate(inorder) if x == 0]
        result = []
        for _ in range(numCourses):
            if not nodes:
                return []

            current = nodes.pop()
            if visited[current]:
                continue

            result.append(current)
            visited[current] = True
            neighbors = graph[current]

            for neighbor in neighbors:
                if visited[neighbor]:
                    continue
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0:
                    nodes.append(neighbor)

        return result
