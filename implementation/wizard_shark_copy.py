# https://www.acmicpc.net/problem/23290

GRID_SIZE = 4


def check_grid(y, x):
    return 0 <= y < GRID_SIZE and 0 <= x < GRID_SIZE


def one_copy_fishes_start(fish_grid):
    copied_fishes = []
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            for direction in fish_grid[y][x]:
                copied_fishes.append((y, x, direction))
    return copied_fishes


def two_fishes_move_one_cell(fish_grid, shark, every_step_smells):
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
                  (0, 1), (1, 1), (1, 0), (1, -1)]

    def check_shark(y, x, shark):
        return shark[0] == y and shark[1] == x

    def check_smell(y, x, every_step_smells):
        for smells in every_step_smells:
            for sy, sx in smells:
                if sy == y and sx == x:
                    return True
        return False

    new_fish_grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for fy in range(GRID_SIZE):
        for fx in range(GRID_SIZE):
            for direction in fish_grid[fy][fx]:
                flag = False
                for i in range(len(directions)):
                    newDirection = (direction - 1 - i) % len(directions) + 1

                    dy, dx = directions[newDirection - 1]
                    ny, nx = fy + dy, fx + dx

                    if not check_grid(ny, nx) or check_shark(ny, nx, shark) or check_smell(ny, nx, every_step_smells):
                        continue

                    new_fish_grid[ny][nx].append(newDirection)
                    flag = True
                    break

                if not flag:
                    new_fish_grid[fy][fx].append(direction)

    return new_fish_grid


def three_shark_move_one_cell(fish_grid, shark, every_step_smells):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    maxCount = 0
    selectedHistory = None

    def dfs(y, x, moveHistory, capturedCount):
        nonlocal maxCount, selectedHistory
        if len(moveHistory) == 3:
            if selectedHistory and capturedCount <= maxCount:
                return

            maxCount = capturedCount
            selectedHistory = moveHistory[:]
            return

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if not check_grid(ny, nx):
                continue

            moveHistory.append((ny, nx))
            visitedCount = visited[ny][nx]
            visited[ny][nx] += 1
            dfs(ny, nx, moveHistory, capturedCount +
                (0 if visitedCount > 0 else len(fish_grid[ny][nx])))
            moveHistory.pop()
            visited[ny][nx] -= 1

    visited = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    dfs(shark[0], shark[1], [], 0)

    this_step_smells = []
    for y, x in selectedHistory:
        if len(fish_grid[y][x]) > 0:
            this_step_smells.append((y, x))
        fish_grid[y][x] = []

    every_step_smells.append(this_step_smells)
    shark[0], shark[1] = selectedHistory[-1]


def four_fish_smell_disappear(every_step_smells):
    if len(every_step_smells) > 2:
        every_step_smells.pop(0)


def five_copy_fishes_finish(fish_grid, copied_fishes):
    for y, x, direction in copied_fishes:
        fish_grid[y][x].append(direction)


def magic_turn(fish_grid, every_step_smells):
    copied_fishes = one_copy_fishes_start(fish_grid)

    fish_grid_after_two = two_fishes_move_one_cell(
        fish_grid, shark, every_step_smells)

    three_shark_move_one_cell(
        fish_grid_after_two, shark, every_step_smells)

    four_fish_smell_disappear(every_step_smells)

    five_copy_fishes_finish(fish_grid_after_two, copied_fishes)

    return fish_grid_after_two


[M, S] = map(int, input().split())
fish_grid = [[[] for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for _ in range(M):
    fy, fx, d = map(int, input().split())
    fish_grid[fy-1][fx-1].append(d)

shark = (list(map(lambda x: int(x) - 1, input().split())))


every_step_smells = []
for _ in range(S):
    fish_grid = magic_turn(fish_grid, every_step_smells)

answer = 0
for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
        answer += len(fish_grid[y][x])

print(answer)
