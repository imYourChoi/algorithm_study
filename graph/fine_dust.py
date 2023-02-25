# https://www.acmicpc.net/problem/17144

import sys
input = sys.stdin.readline

R,C,T = map(int, input().split())
house = [[[each, 0] for each in list(map(int, input().split()))] for _ in range(R)]
cleaner = []
dust = set()
total = 0

for y,row in enumerate(house):
    if row[0][0] == -1:
        cleaner.append((y,0))

for y, row in enumerate(house):
    for x, each in enumerate(row):
        if each[0] > 0:
            dust.add((y,x))
            total += each[0]

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def spread():
    for y in range(R):
        for x in range(C):
            if (y,x) in cleaner or not house[y][x][0]:
                continue
            amount = house[y][x][0] // 5
            count = 0
            for dy,dx in directions:
                Y,X = y+dy, x+dx
                if not 0<=Y<R or not 0<=X<C or (Y,X) in cleaner:
                    continue
                house[Y][X][1] += amount
                count += 1
            house[y][x][0] -= count * amount
    for y in range(R):
        for x in range(C):
            if (y,x) in cleaner:
                continue
            house[y][x][0] += house[y][x][1]
            house[y][x][1] = 0


def clean():
    global total
    for y in range(cleaner[0][0], 0, -1):
        house[y][0][0] = house[y-1][0][0]
    for y in range(cleaner[1][0], R-1):
        house[y][0][0] = house[y+1][0][0]
    for y,x in cleaner:
        total -= house[y][x][0]
        house[y][x][0] = 0
    for x in range(C-1):
        house[0][x][0] = house[0][x+1][0]
        house[R-1][x][0] = house[R-1][x+1][0]
    for y in range(0,cleaner[0][0]):
        house[y][C-1][0] = house[y+1][C-1][0]
    for y in range(R-1, cleaner[1][0],-1):
        house[y][C-1][0] = house[y-1][C-1][0]
    for x in range(C-1,0,-1):
        house[cleaner[0][0]][x][0] = house[cleaner[0][0]][x-1][0]
        house[cleaner[1][0]][x][0] = house[cleaner[1][0]][x-1][0]
    for y,x in cleaner:
        house[y][x][0] = -1

for _ in range(T):
    spread()
    clean()

print(total)