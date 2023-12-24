# https://www.acmicpc.net/problem/4485

import heapq
import sys
input = sys.stdin.readline

inf = float('inf')

answers = []

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def isValid(y, x, n):
    return y >= 0 and y < n and x >= 0 and x < n


while True:
    if not (n := int(input())):
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    distances = [[inf for _ in range(n)] for _ in range(n)]

    heap = [(cave[0][0], (0, 0))]
    distances[0][0] = cave[0][0]

    while heap:
        cur_distance, cur_location = heapq.heappop(heap)
        y, x = cur_location

        if distances[y][x] < cur_distance:
            continue

        for dy, dx in directions:
            Y, X = y+dy, x+dx
            if not isValid(Y, X, n):
                continue
            temp_distance = cur_distance + cave[Y][X]
            if temp_distance < distances[Y][X]:
                distances[Y][X] = temp_distance
                heapq.heappush(heap, (temp_distance, [Y, X]))

    answers.append(distances[n-1][n-1])

for idx, answer in enumerate(answers):
    print(f'Problem {idx+1}: {answer}')
