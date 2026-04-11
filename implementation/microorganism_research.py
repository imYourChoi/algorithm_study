# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/microbial-research/description

from collections import defaultdict
from collections import deque


def check(y, x):
    return 0 <= y < N and 0 <= x < N


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def first(grid, N, rect, id):
    """
    1단계: 미생물 투입 및 쪼개짐 판별
    """
    r1, c1, r2, c2 = rect

    affected_ids = set()

    # 1. 덮어씌워질 위치에 있어 영향을 받는 기존 미생물 ID 모으기
    # 2. 새로운 미생물 덮어쓰기
    for y in range(r1, r2):
        for x in range(c1, c2):
            if grid[y][x] != 0:
                affected_ids.add(grid[y][x])
            grid[y][x] = id

    # 3. 영향받은 미생물들이 쪼개졌는지 검사 (BFS 활용)
    for id in affected_ids:
        cells = []
        for y in range(N):
            for x in range(N):
                if grid[y][x] == id:
                    cells.append((y, x))

        if not cells:
            continue  # 완전히 덮어씌워져 소멸됨

        sy, sx = cells[0]
        q = deque([(sy, sx)])
        visited = {(sy, sx)}

        while q:
            cy, cx = q.popleft()
            for dy, dx in directions:
                ny, nx = cy + dy, cx + dx
                if not check(ny, nx) or (ny, nx) in visited or grid[ny][nx] != id:
                    continue

                visited.add((ny, nx))
                q.append((ny, nx))

        # 탐색된 칸 수와 실제 남은 칸 수가 다르면 쪼개진 것 -> 즉시 삭제
        if len(visited) != len(cells):
            for y, x in cells:
                grid[y][x] = 0

    return grid


def second(grid, N):
    """
    2단계: 미생물 이동 및 정규화 배치
    """
    areas = {}
    shapes = {}

    # 1. 격자 전체를 스캔하여 미생물 정보 추출
    for y in range(N):
        for x in range(N):
            id = grid[y][x]
            if id != 0:
                areas[id] = areas.get(id, 0) + 1
                if id not in shapes:
                    shapes[id] = []
                shapes[id].append((y, x))

    # 넓이(내림차순), 투입 시간(오름차순)으로 정렬
    alive_ids = list(areas.keys())
    alive_ids.sort(key=lambda id: (-areas[id], id))

    new_grid = [[0] * N for _ in range(N)]

    # 2. 정렬된 순서대로 새 격자에 배치
    for id in alive_ids:
        cells = shapes[id]

        # 형태 정규화
        min_y = min(c[0] for c in cells)
        min_x = min(c[1] for c in cells)
        normalized = [(y - min_y, x - min_x) for y, x in cells]

        placed = False

        # x좌표 최소화, 그 다음 y좌표 최소화하며 탐색 (구현에서는 반대)
        for sy in range(N):
            if placed:
                break
            for sx in range(N):
                fits = True
                for dy, dx in normalized:
                    ny, nx = sy + dy, sx + dx
                    if ny >= N or nx >= N or new_grid[ny][nx] != 0:
                        fits = False
                        break

                if fits:
                    # 배치 성공
                    for dy, dx in normalized:
                        new_grid[sy + dy][sx + dx] = id
                    placed = True
                    break

    return new_grid


def third(grid, N):
    """
    3단계: 실험 결과 기록 (인접 쌍의 성과 합산)
    """
    areas = {}
    for y in range(N):
        for x in range(N):
            id = grid[y][x]
            if id != 0:
                areas[id] = areas.get(id, 0) + 1

    pairs = set()

    # 우측, 상단 방향만 체크하여 유니크한 인접 쌍 탐색
    for y in range(N):
        for x in range(N):
            id1 = grid[y][x]
            if id1 == 0:
                continue

            for dy, dx in [(1, 0), (0, 1)]:  # 우, 상
                ny, nx = y + dy, x + dx
                if ny >= N or nx >= N:
                    continue

                id2 = grid[ny][nx]
                if id2 != 0 and id1 != id2:
                    pairs.add((min(id1, id2), max(id1, id2)))

    score = 0
    for p1, p2 in pairs:
        score += areas[p1] * areas[p2]

    return score


# N: 격자 크기, M: 턴(미생물 투입) 횟수
# (문제의 실제 입력 파싱 방식에 맞게 조정하세요)
N, Q = map(int, input().split())

grid = [[0] * N for _ in range(N)]

for id in range(1, Q+1):
    r1, c1, r2, c2 = map(int, input().split())

    # 1단계: 투입 및 쪼개짐 검사
    grid = first(grid, N, (r1, c1, r2, c2), id)
    # if id > 2: print(*grid, sep="\n", end="\n\n")
    # 2단계: 미생물 이동
    grid = second(grid, N)
    # if id > 2: print(*grid, sep="\n", end="\n\n")

    # # 3단계: 점수 계산
    ans = third(grid, N)
    print(ans)
