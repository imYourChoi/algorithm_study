# https://leetcode.com/problems/valid-sudoku/description/

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(r):
            record = set()
            for i in range(9):
                if board[r][i] == ".":
                    continue

                if board[r][i] in record:
                    return False

                record.add(board[r][i])

            return True

        def checkCol(c):
            record = set()
            for i in range(9):
                if board[i][c] == ".":
                    continue

                if board[i][c] in record:
                    return False

                record.add(board[i][c])
            return True

        def checkBox(x):
            record = set()
            Y = (x // 3) * 3
            X = (x % 3) * 3

            for y in range(3):
                for x in range(3):
                    if board[Y+y][X+x] == ".":
                        continue

                    if board[Y+y][X+x] in record:
                        return False

                    record.add(board[Y+y][X+x])

            return True

        for i in range(9):
            if not (checkRow(i) and checkCol(i) and checkBox(i)):
                return False

        return True
