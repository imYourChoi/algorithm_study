# https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())

def Z(N, r, c, row, column):
    if N == 1:
        return c - column if r == row else c - column + 2
    else:
        l = 2 ** (N-1)
        num = 0
        for y in range(row, row+l+1, l):
            for x in range(column, column+l+1, l):
                if y <= r < y+l and x <= c < x+l:
                    return num + Z(N-1, r, c, y, x)
                elif y <= r:
                    num += 2 ** (2*N - 2) 

print(Z(N, r, c, 0, 0))