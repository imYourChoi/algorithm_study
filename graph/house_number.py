# https://www.acmicpc.net/problem/2667

from collections import deque
N = int(input())
array = [list(map(int, [*input()])) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
answer = []

def bfs(row, column):
    global N
    visited[row][column] = True
    num = 0
    queue = deque([[row, column]])

    while queue:
        current = queue.popleft()
        num += 1
        for upDown, leftRight in directions:
            r = current[0] + upDown
            l = current[1] + leftRight
            if not -1 < r < N or not -1 < l < N:
                continue
            if visited[r][l] or not array[r][l]:
                continue
            visited[r][l] = True
            queue.append([r, l])
    return num

def traverse():
    for row in range(N):
        for column in range(N):
            if not array[row][column] or visited[row][column]:
                continue
            answer.append(bfs(row, column))

traverse()
print(len(answer))
for val in sorted(answer):
    print(val)