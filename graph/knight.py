# https://www.acmicpc.net/problem/7562

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
answer = []

directions = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

def bfs(size, start, end):
    array = [[False] * size for _ in range(size)]
    queue = deque([start])
    way = 0

    if start == end:
        return way

    while queue:
        way += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                if not 0 <= x + dx < size or not 0 <= y + dy < size:
                    continue
                if array[y+dy][x+dx]:
                    continue
                if x+dx == end[0] and y+dy == end[1]:
                    return way
                array[y+dy][x+dx] = True
                queue.append([x+dx, y+dy])

for _ in range(N):
    size = int(input())
    start = list(map(int, input().rstrip().split()))
    end = list(map(int, input().rstrip().split()))
    answer.append(bfs(size, start, end))

for x in answer:
    print(x)