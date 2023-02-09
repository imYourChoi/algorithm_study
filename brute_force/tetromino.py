# https://www.acmicpc.net/problem/14500

n,m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
# blocksRot = [
#     [[0,0], [1,0], [2,0], [2,1]],
#     [[0,0], [1,0], [1,1], [2,1]],
#     [[0,0], [0,1], [0,2], [1,1]],
# ]
tetris=[[(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(1,0),(0,1),(1,1)],
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,1),(1,1),(2,1),(2,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(2,0)],
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,2),(1,1),(1,2),(1,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(0,1),(0,2)],
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(1,0),(1,1),(0,1),(0,2)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(0,2),(1,1)],
        [(0,0),(1,0),(1,1),(2,0)],
        [(0,1),(1,1),(1,0),(2,1)]]

score = 0

# for y in range(n):
#     for x in range(m-3):
#         temp = sum(paper[y][x:x+4])
#         score = max(score, temp)

# for y in range(n-3):
#     for x in range(m):
#         temp = sum(paper[y:y+4][x])
#         score = max(score, temp)

# for y in range(n-1):
#     for x in range(m-1):
#         temp = paper[y][x] + paper[y][x+1] + paper[y+1][x] +paper[y+1][x+1]
#         score = max(score, temp)

def isValid(block, y, x):
    for dy,dx in block:
        if not 0<=y+dy<n or not 0<=x+dx<m:
            return False
    return True

def put(y,x):
    value = 0
    for block in tetris:
        # copy = block.copy()
        # for i in range(4):
        #     for each in copy:
        #         each[0], each[1] = each[1], -each[0]
        if not isValid(block, y, x): continue
        temp = 0
        for dy, dx in block:
            Y,X = y+dy, x+dx
            temp += paper[Y][X]
        value = max(value, temp)
    return value

for y in range(n):
    for x in range(m):
        score = max(score, put(y,x))

print(score)