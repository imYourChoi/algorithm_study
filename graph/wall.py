# https://www.acmicpc.net/problem/2206

from collections import deque
import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
array = [list(map(int, [*input().rstrip()])) for _ in range(N)]
arrayBreak = copy.deepcopy(array)
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    way = 1
    global N, M
    queue = deque([ [(0,0), 0] ])
    if N == 1 and M == 1:
        return 1

    while queue:
        way += 1
        for _ in range(len(queue)):
            current, breaked = queue.popleft()
            x, y = current
            for dx, dy in directions:
                moveTo = (x + dx, y + dy)
                if moveTo == (M-1, N-1):
                    return way
                if not 0 <= moveTo[0] < M or not 0 <= moveTo[1] < N:
                    continue
                if array[y+dy][x+dx] == 1:
                    if not breaked:
                        arrayBreak[y+dy][x+dx] = -1
                        queue.append([moveTo, 1])
                    continue
                if breaked:
                    if arrayBreak[y+dy][x+dx] == -1:
                        continue
                    arrayBreak[y+dy][x+dx] = -1
                    queue.append([moveTo, breaked])
                    continue
                if array[y+dy][x+dx] == -1:
                    continue
                array[y+dy][x+dx] = -1
                queue.append([moveTo, breaked])
    return -1
print(bfs())