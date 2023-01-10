# https://www.acmicpc.net/problem/7569

from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
array = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
rotten = []

for hei in range(H):
    for row in range(N):
        for col in range(M):
            if array[hei][row][col] > 0:
                rotten.append([hei,row,col])

directions = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]

def bfs():
    global N, M, H
    way = -1
    queue = deque(rotten)
    
    while queue:
        for _ in range(len(queue)):
            h, y, x = queue.popleft()
            for dh, dy, dx in directions:
                if not 0 <= h + dh < H or not 0 <= x + dx < M or not 0 <= y + dy < N:
                    continue
                if array[h + dh][y + dy][x + dx] != 0:
                    continue
                array[h + dh][y + dy][x + dx] = 1
                queue.append([h+dh, y+dy, x+dx])
        way += 1
    print(array.count(0))
    for hei in array:
        for row in hei:
            for col in row:
                if col == 0:
                    return -1
    return way

print(bfs())