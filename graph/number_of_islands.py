# https://leetcode.com/problems/number-of-islands/


from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def check(y, x):
            return 0 <= y < m and 0 <= x < n

        def dfs(y, x):
            if not check(y, x) or grid[y][x] != '1':
                return

            grid[y][x] = '-1'
            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)

        def bfs(y, x):
            queue = deque([(y, x)])

            while queue:
                cy, cx = queue.popleft()

                for dy, dx in directions:
                    ny, nx = cy + dy, cx + dx

                    if not check(ny, nx) or grid[ny][nx] != "1":
                        continue

                    grid[ny][nx] = "-1"
                    queue.append((ny, nx))

        m, n = len(grid), len(grid[0])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        answer = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    bfs(y, x)
                    # dfs(y, x)
                    answer += 1

        return answer
