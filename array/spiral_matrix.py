# https://leetcode.com/problems/spiral-matrix/description/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        nx, ny = len(matrix[0]), len(matrix) - 1

        direction = 0
        answer = []
        x, y = -1, 0

        while nx >= 0 and ny >= 0:
            if direction == 0 or direction == 2:
                if nx == 0:
                    break
                dy, dx = directions[direction]
                for i in range(nx):
                    x += dx
                    answer.append(matrix[y][x])
                nx -= 1
            else:
                if ny == 0:
                    break
                dy, dx = directions[direction]
                for i in range(ny):
                    y += dy
                    answer.append(matrix[y][x])
                ny -= 1
            direction = (direction + 1) % 4

        return answer
