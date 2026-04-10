# https://www.acmicpc.net/problem/23291

N, K = map(int, input().split())

bowls = list(map(int, input().split()))
bowls = [bowls] + [[0] * N for _ in range(N)]


def first_increment(bowls):
    minimum = float('inf')
    minimumBowls = []

    for i, bowl in enumerate(bowls[0]):
        if bowl < minimum:
            minimum = bowl
            minimumBowls = [(i, bowl)]
        elif bowl == minimum:
            minimumBowls.append((i, bowl))

    for i, bowl in minimumBowls:
        bowls[0][i] += 1

    # print(*bowls, sep="\n", end="\n\n")


def second_levitate(bowls):
    def step(start, end, height):
        width = end - start + 1
        for x in range(width):
            for y in range(height):
                bowls[width - x][end+1+y] = bowls[y][start+x]
                bowls[y][start+x] = 0

    height = 1
    remain = N
    start, end = 0, 0
    while height < remain:
        step(start, end, height)
        remain -= height
        start, end, height = end + 1, end + height, end - start + 1 + 1

    # print(*bowls, sep="\n", end="\n\n")
    return start, end, height


def check(y, x):
    return 0 <= y < N and 0 <= x < N


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def third_control_fish(bowls):
    diffs = []

    def bfs(y, x):
        visited = [[False] * N for _ in range(N)]
        queue = [(y, x)]

        while queue:
            temp = []
            for cy, cx in queue:
                if visited[cy][cx]:
                    continue

                visited[cy][cx] = True

                for dy, dx in directions:
                    ny, nx = cy + dy, cx + dx
                    if not check(ny, nx) or visited[ny][nx] or bowls[ny][nx] == 0:
                        continue

                    d = abs(bowls[ny][nx] - bowls[cy][cx]) // 5
                    if d > 0:
                        if bowls[ny][nx] > bowls[cy][cx]:
                            diffs.append(((ny, nx), (cy, cx), d))
                        else:
                            diffs.append(((cy, cx), (ny, nx), d))

                    temp.append((ny, nx))

            queue = temp

    bfs(0, N-1)

    for (fy, fx), (ty, tx), d in diffs:
        bowls[fy][fx] -= d
        bowls[ty][tx] += d

    # print(*bowls, sep="\n", end="\n\n")


def fourth_align(bowls, start, end, height):
    for x in range(start, end+1):
        for y in range(height):
            bowls[0][height * (x-start) + y] = bowls[y][x]
            bowls[y][x] = 0

    # print(*bowls, sep="\n", end="\n\n")


def fifth_levitate(bowls):

    def move(start, end, height):
        for x in range(end-start+1):
            for y in range(height):
                bowls[height+(height-y)-1][N-1-x] = bowls[y][start+x]
                bowls[y][start+x] = 0
                # print(height+(height-y)-1, N-1-x, y, start+x)

    move(0, N//2-1, 1)
    move(N//2, N//4*3-1, 2)

    # print(*bowls, sep="\n", end="\n\n")


count = 0
while True:
    count += 1

    first_increment(bowls)
    start, end, height = second_levitate(bowls)
    third_control_fish(bowls)
    fourth_align(bowls, start, end, height)
    fifth_levitate(bowls)
    third_control_fish(bowls)
    fourth_align(bowls, N//4*3, N-1, 4)

    # print(bowls[0])
    # break
    if abs(max(bowls[0]) - min(bowls[0])) <= K:
        break

print(count)
