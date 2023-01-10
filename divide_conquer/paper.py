# https://www.acmicpc.net/problem/1780

import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
array = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]

def check(num): # -1, 0, 1
    if num == 1:
        return 0, 0, 1
    elif num == 0:
        return 0, 1, 0
    else:
        return 1, 0, 0

def paper(array, row, column, index):
    base = array[row][column]
    if index == 1:
        return check(base)
    flag = True
    for r in range(row, row + index):
        for c in range(column, column + index):
            if array[r][c] != base:
                step = index // 3
                minus, zero, one = 0, 0, 0
                for r2 in range(row, row+index, step):
                    for c2 in range(column, column+index, step):
                        m, z, o = paper(array, r2, c2, step)
                        minus += m
                        zero += z
                        one += o
                return minus, zero, one
    # if flag == False:
    #     step = index // 3
    #     minus, zero, one = 0, 0, 0
    #     for r in range(row, row+index, step):
    #         for c in range(column, column+index, step):
    #             m, z, o = paper(array, r, c, step)
    #             minus += m
    #             zero += z
    #             one += o
    #     return minus, zero, one
    return check(base)

minus, zero, one = paper(array, 0, 0, n)

print(minus)
print(zero)
print(one)