# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/frog-journey/description

import heapq

N = int(input())

lake = [list(input()) for _ in range(N)]

Q = int(input())

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check_grid(y, x):
    return 0 <= y < N and 0 <= x < N


precalculatedStones = [[[] for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(N):
        for dy, dx in directions:
            for i in range(1, 6):
                ny, nx = y + (dy * i), x + (dx * i)
                if not check_grid(ny, nx):
                    continue
                if lake[ny][nx] == "#":
                    break
                if lake[ny][nx] == "S":
                    continue

                precalculatedStones[y][x].append((ny, nx, i))


def calculateDist(curJump, newJump):
    if curJump >= newJump:
        return 1
    else:
        time = 0
        for i in range(curJump+1, newJump+1):
            time += i ** 2
        return time


def travel():
    r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())

    distances = [[[float('inf')] * 6 for _ in range(N)] for _ in range(N)]

    distances[r1][c1][1] = 0
    heap = [(0, (r1, c1), 1)]

    while heap:
        dist, (cy, cx), curJump = heapq.heappop(heap)

        if cy == r2 and cx == c2:
            break

        if distances[cy][cx][curJump] < dist:
            continue

        stones = precalculatedStones[cy][cx]

        for sy, sx, newJump in stones:
            dist = calculateDist(curJump, newJump)
            if newJump == curJump:
                newDist = distances[cy][cx][newJump] + 1
                if newDist < distances[sy][sx][newJump]:
                    distances[sy][sx][newJump] = newDist
                    heapq.heappush(heap, (newDist, (sy, sx), newJump))
            else:
                newJumpDist = distances[cy][cx][curJump] + dist
                if newJumpDist > distances[cy][cx][newJump]:
                    continue
                distances[cy][cx][newJump] = newJumpDist

                newMoveDist = newJumpDist + 1
                if newMoveDist >= distances[sy][sx][newJump]:
                    continue
                distances[sy][sx][newJump] = newMoveDist
                heapq.heappush(heap, (newMoveDist, (sy, sx), newJump))

    if all(x == float('inf') for x in distances[r2][c2]):
        print(-1)
    else:
        print(min(distances[r2][c2]))


for _ in range(Q):
    travel()
