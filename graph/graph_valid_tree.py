# https://neetcode.io/problems/valid-tree/question


from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        for x, y in edges:
            graph[y].append(x)
            graph[x].append(y)

        print(graph)

        visited = [False] * n
        total = 1

        def dfs(current, parent):
            nonlocal total
            for neighbor in graph[current]:
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    return False

                visited[neighbor] = True

                total += 1
                if not dfs(neighbor, current):
                    return False

            return True

        return dfs(0, -1) and total == n
