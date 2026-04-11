# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/mint-choco-milk/description

import heapq

N, T = map(int, input().split())

foodGrid = [list(map(set, input())) for _ in range(N)]
faithGrid = [list(map(int, input().split())) for _ in range(N)]


def morning():
    for y in range(N):
        for x in range(N):
            faithGrid[y][x] += 1


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check(y, x):
    return 0 <= y < N and 0 <= x < N


def lunch():
    groups = [None, [], [], []]

    visited = [[False] * N for _ in range(N)]

    def bfs(y, x):
        visited[y][x] = True

        queue = [(y, x)]
        groupMembers = [(y, x)]

        leaderFaith = faithGrid[y][x]
        leaderCandid = [(y, x)]

        while queue:
            temp = []
            for i in range(len(queue)):
                cy, cx = queue[i]

                for dy, dx in directions:
                    ny, nx = cy + dy, cx + dx

                    if not check(ny, nx) or visited[ny][nx] or foodGrid[ny][nx] != foodGrid[cy][cx]:
                        continue

                    visited[ny][nx] = True
                    temp.append((ny, nx))
                    groupMembers.append((ny, nx))

                    faith = faithGrid[ny][nx]
                    if leaderFaith < faith:
                        leaderFaith = faith
                        leaderCandid = [(ny, nx)]
                    elif leaderFaith == faith:
                        leaderCandid.append((ny, nx))

            queue = temp

        leaderCandid.sort()
        leaderLocation = leaderCandid[0]

        return leaderLocation, groupMembers

    def hand_to_leader(ly, lx, groupMembers):
        for my, mx in groupMembers:
            if my == ly and mx == lx:
                faithGrid[my][mx] += len(groupMembers) - 1
            else:
                faithGrid[my][mx] -= 1

    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                continue
            (ly, lx), groupMembers = bfs(y, x)
            hand_to_leader(ly, lx, groupMembers)

            groupFood = foodGrid[y][x]

            heapq.heappush(groups[len(groupFood)],
                           (-faithGrid[ly][lx], ly, lx))

    return groups


def dinner(groups):
    spreadedSet = set()
    for i in range(1, 4):
        while groups[i]:
            faith, ly, lx = heapq.heappop(groups[i])
            faith *= -1

            if (ly, lx) in spreadedSet:
                continue
            leaderFood = foodGrid[ly][lx]

            B = faithGrid[ly][lx]
            d = B % 4
            x = B - 1
            faithGrid[ly][lx] = 1

            dy, dx = directions[d]
            ny, nx = ly + dy, lx + dx
            while check(ny, nx) and x > 0:
                if foodGrid[ny][nx] == leaderFood:
                    pass
                else:
                    spreadedSet.add((ny, nx))
                    y = faithGrid[ny][nx]
                    if x > y:
                        x -= y + 1
                        faithGrid[ny][nx] += 1
                        foodGrid[ny][nx] = leaderFood.copy()
                        if x == 0:
                            break
                    else:
                        foodGrid[ny][nx].update(leaderFood)
                        faithGrid[ny][nx] += x
                        x = 0

                ny += dy
                nx += dx


tcm = set(["T", "C", "M"])
tc = set(["T", "C"])
tm = set(["T", "M"])
cm = set(["C", "M"])
m = set(["M"])
c = set(["C"])
t = set(["T"])


def check_food_type(food):
    return [tcm, tc, tm, cm, m, c, t].index(food)


def count_faith():
    counts = [0] * 7
    for y in range(N):
        for x in range(N):
            type = check_food_type(foodGrid[y][x])
            counts[type] += faithGrid[y][x]

    print(" ".join(map(str, counts)))


for _ in range(T):
    morning()

    groups = lunch()

    dinner(groups)

    count_faith()
