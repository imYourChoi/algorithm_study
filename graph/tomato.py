# https://www.acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
array = [list(map(int, input().rstrip().split())) for _ in range(N)]
rotten = []

for row in range(N):
    for col in range(M):
        if array[row][col] > 0:
            rotten.append([row,col])

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    global N, M
    way = -1
    queue = deque(rotten)
    
    while queue:
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in directions:
                if not 0 <= x + dx < M or not 0 <= y + dy < N:
                    continue
                if array[y + dy][x + dx] != 0:
                    continue
                array[y + dy][x + dx] = 1
                queue.append([y+dy, x+dx])
        way += 1
    
    for row in array:
        for col in row:
            if col == 0:
                return -1
    return way

print(bfs())