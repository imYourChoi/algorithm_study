# https://www.acmicpc.net/problem/2447

import sys
sys.setrecursionlimit(10 ** 8)
n = int(input())
array=[[" "]*n for _ in range(n)]

def rec(size, row, column):
    if size == 3:
        for r in range(row, row+3):
            for c in range(column, column+3):
                if r == row+1 and c== column + 1:
                    continue
                array[r][c]="*"
        return
    

    for i in range(9):
        if i == 4: continue
        rec(size//3, row + i // 3 * (size // 3), column + i % 3 * (size // 3))

rec(n, 0, 0)

for x in array:
    print("".join(x))