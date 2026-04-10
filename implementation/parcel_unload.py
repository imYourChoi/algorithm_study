# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/delivery-service/description

N, M = map(int, input().split())

parcels = [list(map(int, input().split())) for _ in range(M)]

grid = [[-1]*N for _ in range(N)]


def gravity(k, h, w, c, r, existing):
    fy = None
    for y in range(r+h, N):
        blocked = False
        for x in range(c, c+w):
            if grid[y][x] != -1:
                blocked = True
                break

        if blocked:
            fy = y
            break

    if not fy:
        fy = N

    for sy in range(fy-h, fy):
        for sx in range(c, c+w):
            grid[sy][sx] = k

    if existing:
        for ey in range(r, fy-h):
            for ex in range(c, c+w):
                grid[ey][ex] = -1

    parcelDict[k][3] = fy-h


def check_unload(h, w, c, r, direction):
    xRange = range(c-1, -1, -1) if direction == 'left' else range(c+w, N)
    for x in xRange:
        for y in range(r, r+h):
            if grid[y][x] != -1:
                return False
    return True


def unload(direction):
    minimum = 101
    for key, value in parcelDict.items():
        if check_unload(*value, direction):
            minimum = min(minimum, key)

    h, w, c, r = parcelDict[minimum]

    for y in range(r, r + h):
        for x in range(c, c + w):
            grid[y][x] = -1

    parcelDict.pop(minimum)
    print(minimum)


parcelDict = {}
for k, h, w, c in parcels:
    c -= 1
    parcelDict[k] = [h, w, c, None]
    gravity(k, h, w, c, 0, False)

while parcelDict:
    unload("left")
    for k, [h, w, c, r] in parcelDict.items():
        gravity(k, h, w, c, r, True)
    unload("right")
    for k, [h, w, c, r] in parcelDict.items():
        gravity(k, h, w, c, r, True)
