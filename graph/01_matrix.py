# https://leetcode.com/problems/01-matrix/description/

from collections import deque
from typing import List


def check(y, x, R, C):
    return 0 <= y < R and 0 <= x < C


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        R, C = len(mat), len(mat[0])

        zeros = []
        for y in range(R):
            for x in range(C):
                if mat[y][x] == 0:
                    zeros.append((y, x))
                else:
                    mat[y][x] = -1

        queue = deque(zeros)

        while queue:
            ny, nx = queue.popleft()
            for dy, dx in directions:
                y, x = ny + dy, nx + dx
                if not check(y, x, R, C) or mat[y][x] != -1:
                    continue

                mat[y][x] = mat[ny][nx] + 1

                queue.append((y, x))

        return mat
