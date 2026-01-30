# https://leetcode.com/problems/minimum-height-trees/description/

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent, length):
            if length > nodeInfo[0]:
                nodeInfo[0] = length
                nodeInfo[1] = node

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node, length + 1)

        def dfsPath(node, parent, length):
            if length > maxInfo[0]:
                maxInfo[0] = length
                maxInfo[1] = node

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                parentMap[neighbor] = node
                dfsPath(neighbor, node, length + 1)

        nodeInfo = [0, None]
        dfs(0, -1, 0)

        maxInfo = [-1, None]
        parentMap = {nodeInfo[1]: -1}
        dfsPath(nodeInfo[1], -1, 0)

        path = []
        cur = maxInfo[1]
        while cur != -1:
            path.append(cur)
            cur = parentMap[cur]

        l = len(path)
        return path[(l-1)//2: l//2+1]
