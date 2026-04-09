# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/ai-robot/description

from collections import deque

N, K, L = map(int, input().split())

dustGrid = [list(map(int, input().split())) for _ in range(N)]

robots = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def check_grid(y, x):
    return 0 <= y < N and 0 <= x < N


def one_robots_move(dustGrid, robots):
    newRobots = []
    robotsLocation = [[False] * N for _ in range(N)]

    for ry, rx in robots:
        robotsLocation[ry][rx] = True

    def bfs(y, x):
        visited = [[False] * N for _ in range(N)]
        visited[y][x] = True

        queue = deque([(y, x)])

        flag = False
        candids = []

        while queue:
            for _ in range(len(queue)):
                cy, cx = queue.popleft()

                for dy, dx in directions:
                    ny, nx = cy + dy, cx + dx

                    if not check_grid(ny, nx) or visited[ny][nx] or dustGrid[ny][nx] == -1 or robotsLocation[ny][nx]:
                        continue

                    if dustGrid[ny][nx] > 0:
                        flag = True
                        candids.append((ny, nx))

                    visited[ny][nx] = True
                    queue.append((ny, nx))

            if flag:
                break

        if flag:
            candids.sort()
            return candids[0]
        return y, x

    for ry, rx in robots:
        if dustGrid[ry][rx] > 0:
            newRobots.append((ry, rx))
            continue

        robotsLocation[ry][rx] = False
        ny, nx = bfs(ry, rx)
        robotsLocation[ny][nx] = True
        newRobots.append((ny, nx))

    return newRobots


def two_clean(dustGrid, robots):
    cleanDirections = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    newDustGrid = [c[:] for c in dustGrid]

    def get_sum_of_adjacent(y, x):
        temp = 0
        for dy, dx in cleanDirections:
            ny, nx = y + dy, x + dx
            if not check_grid(ny, nx) or newDustGrid[ny][nx] == -1:
                continue
            temp += min(20, newDustGrid[ny][nx])

        return temp

    def find_max_direction(y, x):

        adjacentDustSum = get_sum_of_adjacent(y, x)
        tempDirection = -1
        maxDustSum = -1

        for i in range(4):
            oy, ox = cleanDirections[(i + 2) % 4]
            ny, nx = y + oy, x + ox

            curDustSum = adjacentDustSum
            if check_grid(ny, nx) and newDustGrid[ny][nx] > 0:
                curDustSum -= min(newDustGrid[ny][nx], 20)
            if curDustSum > maxDustSum:
                tempDirection = i
                maxDustSum = curDustSum

        return tempDirection

    for ry, rx in robots:
        maxDirection = find_max_direction(ry, rx)
        newDustGrid[ry][rx] = max(0, newDustGrid[ry][rx] - 20)
        for i, (dy, dx) in enumerate(cleanDirections):
            if i == (maxDirection + 2) % 4:
                continue
            ny, nx = ry + dy, rx + dx
            if not check_grid(ny, nx) or newDustGrid[ny][nx] == -1:
                continue
            newDustGrid[ny][nx] = max(0, newDustGrid[ny][nx] - 20)

    return newDustGrid


def three_dust_acc(dustGrid):
    for y in range(N):
        for x in range(N):
            if dustGrid[y][x] > 0:
                dustGrid[y][x] += 5


def four_dust_spread(dustGrid):
    spreads = []
    for y in range(N):
        for x in range(N):
            if dustGrid[y][x] != 0:
                continue

            tempDust = 0

            for dy, dx in directions:
                ny, nx = y + dy, x + dx

                if not check_grid(ny, nx) or dustGrid[ny][nx] == -1:
                    continue

                tempDust += dustGrid[ny][nx]
            if tempDust >= 10:
                spreads.append((y, x, tempDust // 10))

    for y, x, dust in spreads:
        dustGrid[y][x] += dust


def five_print(dustGrid):
    return sum(sum([x for x in row if x > 0]) for row in dustGrid)


def test(dustGrid, robots):
    robots = one_robots_move(dustGrid, robots)
    dustGrid = two_clean(dustGrid, robots)
    three_dust_acc(dustGrid)

    four_dust_spread(dustGrid)

    amount = five_print(dustGrid)

    return amount, dustGrid, robots


for _ in range(L):
    amount, dustGrid, robots = test(dustGrid, robots)
    print(amount)
