# https://www.acmicpc.net/problem/2638

from collections import deque

N,M=map(int, input().split())
paper=[list(map(int, input().split())) for _ in range(N)]

cheeze={(y,x) for y in range(N) for x in range(M) if paper[y][x]}

directions = [(-1,0),(0,1),(1,0),(0,-1)]

def exterior(y,x):
    queue=deque([(y,x)])
    paper[y][x]=2
    while queue:
        for _ in range(len(queue)):
            y,x = queue.popleft()
            for dy,dx in directions:
                Y,X = y+dy, x+dx
                if not 0<=Y<N or not 0<=X<M:
                    continue
                if not paper[Y][X]:
                    queue.append((Y,X))
                    paper[Y][X] = 2

exterior(0,0)
time = 0
while cheeze:
    time += 1
    cheezeCopy = cheeze.copy()
    temp = set()
    for _ in range(len(cheezeCopy)):
        y,x = cheezeCopy.pop()
        airCount = 0
        for dy,dx in directions:
            Y,X = y+dy, x+dx
            if (Y,X) in temp:
                continue
            if not 0<=Y<N or not 0<=X<M:
                continue
            if paper[Y][X] == 2:
                airCount += 1
        if airCount >= 2:
            temp.add((y,x))
    for y,x in temp:
        paper[y][x] = 2
        exterior(y,x)
    cheeze = cheeze - temp

print(time)

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 1 0 0 0 1 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 0 0 1 0 0 1 0
# 0 1 0 1 1 1 0 1 0
# 0 1 1 0 0 0 1 1 0
# 0 0 0 0 0 0 0 0 0