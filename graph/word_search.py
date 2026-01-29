# https://leetcode.com/problems/word-search/description/

from collections import deque
from typing import List


def check(y, x, m, n):
    return 0 <= y < m and 0 <= x < n


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(y, x, i):
            if i == len(word):
                return True

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if (
                    not check(ny, nx, m, n)
                    or board[ny][nx] != word[i]
                    or visited[ny][nx]
                ):
                    continue

                visited[ny][nx] = True
                result = dfs(ny, nx, i + 1)
                visited[ny][nx] = False

                if result:
                    return True

            return False

        for y in range(m):
            for x in range(n):
                if board[y][x] == word[0]:
                    visited[y][x] = True
                    result = dfs(y, x, 1)
                    visited[y][x] = False

                    if result:
                        return True

        return False
