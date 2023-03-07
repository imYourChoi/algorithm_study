# https://www.acmicpc.net/problem/9328

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
answer = []

def checkUpper(str):
    if str >= 'A' and str <= 'Z':
      return True
    else:
      return False

def checkLower(str):
    if str >= 'a' and str <= 'z':
      return True
    else:
      return False

def addEntry(space, temp, keys, y,x):
    global total
    if space == ".":
        temp.append((y,x))
    elif checkLower(space):
        keys.add(space)
        temp.append((y,x))
    elif checkUpper(space):
        temp.append((y,x))
        if space.lower() in keys:
            plan[y][x] = "."
    elif space == "$":
        temp.append((y,x))
        plan[y][x] = "."
        total += 1

def getEntry(plan, keys, h):
    temp = []
    for idx, space in enumerate(plan[0]):
        addEntry(space, temp, keys, 0, idx)
    for idx, space in enumerate(plan[-1]):
        addEntry(space, temp, keys, h-1, idx)
    for idx, row in enumerate(plan[1:-1]):
        for space, x in [(row[0], 0), (row[-1], w-1)]:
            addEntry(space, temp, keys, idx+1, x)
    return temp

directions = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(T):
    h,w = map(int, input().split())
    plan = [list(input().strip()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    keys = set(v if (v := input().strip()) != "0" else [])
    total = 0
    entry = getEntry(plan, keys, h)
    queue = deque(entry)
    while queue:
        flag = True
        for _ in range(len(queue)):
            y,x = queue.popleft()
            if checkUpper(plan[y][x]):
                if plan[y][x].lower() in keys:
                    plan[y][x] = "."
                    flag = False
                else:
                    queue.append((y,x))
                    continue
            for dy,dx in directions:
                Y,X = y+dy,x+dx
                if not 0<=Y<h or not 0<=X<w:
                    continue
                if plan[Y][X] == "*" or visited[Y][X]:
                    continue
                visited[Y][X] = True
                flag = False
                if checkLower(plan[Y][X]):
                    keys.add(plan[Y][X])
                    plan[Y][X] = "."
                    queue.append((Y,X))
                elif checkUpper(plan[Y][X]):
                    queue.append((Y,X))
                elif plan[Y][X] == "$":
                    total += 1
                    plan[Y][X] = "."
                    queue.append((Y,X))
                else:
                    queue.append((Y,X))
        if flag: break
    answer.append(total)

print(*answer, sep="\n")

# https://www.acmicpc.net/board/view/92642
# https://www.acmicpc.net/board/view/69162