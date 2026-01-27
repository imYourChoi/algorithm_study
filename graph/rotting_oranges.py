# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque
from typing import List


def check(y, x, r, c):
    return 0 <= y < r and 0 <= x < c


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque([])
        fresh = 0
        time = 0

        for y in range(r):
            for x in range(c):
                if grid[y][x] == 2:
                    queue.append((y, x))
                elif grid[y][x] == 1:
                    fresh += 1

        while queue and fresh > 0:
            time += 1

            for _ in range(len(queue)):
                cy, cx = queue.popleft()
                for dy, dx in directions:
                    ny, nx = cy + dy, cx + dx
                    if not check(ny, nx, r, c) or grid[ny][nx] != 1:
                        continue

                    grid[ny][nx] = 2
                    fresh -= 1
                    queue.append((ny, nx))

        return time if fresh == 0 else -1
