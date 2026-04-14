# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/a-little-sea-turtles-big-adventure/description

def check(y, x):
    return 0 <= y < N and 0 <= x < N


def first(time):

    def bfs(y, x):
        distances = [[0] * N for _ in range(N)]

        queue = [(N-1, N-1)]
        distance = 0
        reached = False

        while queue:
            distance += 1
            temp = []

            for cy, cx in queue:
                for dy, dx in directions:
                    ny, nx = cy + dy, cx + dx

                    if not check(ny, nx) or distances[ny][nx] > 0 or grid[ny][nx] == 1:
                        continue

                    if ny == y and nx == x:
                        reached = True
                        distances[ny][nx] = distance
                        break

                    if turtleGrid[ny][nx]:
                        continue

                    distances[ny][nx] = distance
                    temp.append((ny, nx))

            if reached:
                break
            queue = temp

        if distances[y][x] == 0:
            return None, None

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if not check(ny, nx):
                continue

            if distances[ny][nx] == distances[y][x] - 1:
                return (ny, nx)

    newTurtles = []

    for i, (ty, tx) in enumerate(turtles):
        if (ty, tx) in stoned:
            newTurtles.append((ty, tx))
        elif ty == -1:
            newTurtles.append((-1, -1))
        else:
            ny, nx = bfs(ty, tx)
            if ny is None:
                newTurtles.append((ty, tx))
            elif ny == N - 1 and nx == N - 1:
                answer[i] = str(time)
                turtleGrid[ty][tx] = False
                newTurtles.append((-1, -1))
            else:
                turtleGrid[ty][tx] = False
                turtleGrid[ny][nx] = True
                newTurtles.append((ny, nx))

    return newTurtles


def second():
    for vy, vx, _ in volcanoes:
        volcanoGrid[vy][vx][0] += 10


def third():
    exploded = set()

    def explode(y, x, p):
        if (y, x) in exploded:
            return

        exploded.add((y, x))

        volcanoGrid[vy][vx][2] += p

        if volcanoGrid[y][x][2] >= 20 and turtleGrid[y][x]:
            stoned.add((y, x))

        for dy, dx in directions:
            curPower = p // 2

            for i in range(1, N):
                ny, nx = y + dy * i, x + dx * i
                if not check(ny, nx) or grid[ny][nx] == 1:
                    break

                volcanoGrid[ny][nx][2] += curPower

                if volcanoGrid[ny][nx][2] >= 20 and turtleGrid[ny][nx]:
                    stoned.add((ny, nx))

                if volcanoGrid[ny][nx][0] + volcanoGrid[ny][nx][2] >= volcanoGrid[ny][nx][1]:
                    explode(ny, nx, volcanoGrid[ny][nx][1])

                curPower //= 2
                if curPower == 0:
                    break

    for vy, vx, p in volcanoes:
        if (vy, vx) in exploded:
            continue
        if volcanoGrid[vy][vx][0] >= volcanoGrid[vy][vx][1]:
            explode(vy, vx, p)

    return exploded


def fourth(exploded):
    for y in range(N):
        for x in range(N):
            volcanoGrid[y][x][2] = 0

    for vy, vx in exploded:
        volcanoGrid[vy][vx][0] = 0


N, M, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

turtles = [list(map(int, input().split())) for _ in range(M)]
turtleGrid = [[False] * N for _ in range(N)]

volcanoes = [list(map(int, input().split())) for _ in range(K)]
volcanoGrid = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

for ty, tx in turtles:
    turtleGrid[ty][tx] = True

for vy, vx, p in volcanoes:
    volcanoGrid[vy][vx][1] = p

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

answer = ["-1"] * M
time = 1

stoned = set()

while time <= 100 and any(x[0] != -1 for x in turtles):
    turtles = first(time)

    second()

    exploded = third()

    fourth(exploded)

    time += 1

print(*answer, sep="\n")
