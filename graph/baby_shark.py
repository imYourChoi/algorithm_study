# https://www.acmicpc.net/problem/16236

from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
first = None
for idx, row in enumerate(space):
    if 9 in row:
        first = (idx, i:=row.index(9))
        row[i] = 0

directions = [(-1, 0), (0,-1), (0,1), (1,0)]

def bfs():
    size = 2
    eaten = 0
    moved = 0
    second = 0
    
    visited = [[False] * n for _ in range(n)]
    visited[first[0]][first[1]] = True
    queue = deque([first])

    while queue:
        flag = False
        # print(queue)
        temp = []
        for _ in range(len(queue)):
            y, x = queue.popleft()
            for dy, dx in directions:
                Y, X = y+dy, x+dx
                if not 0<=Y<n or not 0<=X<n or visited[Y][X]:
                    continue
                if 0 < space[Y][X] < size:
                    temp.append((Y,X))
                    # eaten += 1
                    # space[Y][X] = 0
                    # if eaten == size:
                    #     size += 1
                    #     eaten = 0
                    # queue = deque([(Y,X)])
                    # flag = True
                    # visited = [[False] * n for _ in range(n)]
                    # break
                elif space[Y][X] <= size:
                    queue.append((Y,X))
                    visited[Y][X] = True

            # if flag: break
        moved += 1
        if temp:
            # print(temp)
            temp.sort(key=lambda x: x[1])
            temp.sort(key=lambda x: x[0])
            # print("EATEN \t", temp, size, eaten, end="\n\n")
            Y,X = temp[0]
            space[Y][X] = 0
            eaten += 1
            if eaten == size:
                size += 1
                eaten = 0
            queue = deque([(Y,X)])
            visited = [[False] * n for _ in range(n)]
            visited[Y][X] = True
            second += moved
            moved = 0
            
    print(second)

bfs()