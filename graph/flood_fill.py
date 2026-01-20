# https://leetcode.com/problems/flood-fill/description/

from collections import deque
from typing import List


def check(y, x, r, c):
    return 0 <= y < r and 0 <= x < c


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        r, c = len(image), len(image[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        queue = deque([(sr, sc)])

        original = image[sr][sc]

        while queue:
            print(queue)
            nr, nc = queue.popleft()

            if visited[nr][nc]:
                continue

            visited[nr][nc] = True

            if image[nr][nc] != original:
                continue

            image[nr][nc] = color

            for dy, dx in directions:
                Y, X = nr + dy, nc + dx

                if not check(Y, X, r, c) or visited[Y][X]:
                    continue

                queue.append((Y, X))

        return image
