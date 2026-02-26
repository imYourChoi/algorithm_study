# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        grid = [[[False, False] for _ in range(c)] for _ in range(r)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def check(y, x):
            return 0 <= x < c and 0 <= y < r

        def bfs(queue, visited, ocean):
            while queue:
                temp = []
                for i in range(len(queue)):
                    cy, cx = queue[i]

                    for dy, dx in directions:
                        ny, nx = cy + dy, cx + dx
                        if not check(ny, nx) or visited[ny][nx] or heights[ny][nx] < heights[cy][cx]:
                            continue

                        visited[ny][nx] = True
                        temp.append((ny, nx))
                        grid[ny][nx][ocean] = True

                queue = temp

        def pacific():
            pVisited = [[False for _ in range(c)] for _ in range(r)]
            queue = []
            for i in range(r):
                queue.append((i, 0))
                pVisited[i][0] = True
                grid[i][0][0] = True
            for i in range(1, c):
                queue.append((0, i))
                pVisited[0][i] = True
                grid[0][i][0] = True

            bfs(queue, pVisited, 0)

        def atlantic():
            cVisited = [[False for _ in range(c)] for _ in range(r)]

            queue = []
            for i in range(r):
                queue.append((i, c-1))
                cVisited[i][c-1] = True
                grid[i][c-1][1] = True
            for i in range(c-1):
                queue.append((r-1, i))
                cVisited[r-1][i] = True
                grid[r-1][i][1] = True

            bfs(queue, cVisited, 1)

        pacific()
        atlantic()

        output = []

        for y in range(r):
            for x in range(c):
                if all(grid[y][x]):
                    output.append([y, x])

        return output
