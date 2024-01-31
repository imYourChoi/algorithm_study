# https://www.acmicpc.net/problem/2357
# https://squareyun.tistory.com/103

import math
import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def makeSegmentTree(idx, start, end):
    if start == end:
        segment[idx] = (arr[start], arr[start])
        return segment[idx]

    mid = (start + end) // 2

    left = makeSegmentTree(idx * 2, start, mid)
    right = makeSegmentTree(idx * 2 + 1, mid + 1, end)

    segment[idx] = (min(left[0], right[0]), max(left[1], right[1]))

    return segment[idx]


def find(idx, start, end):
    if b < start or a > end:
        return (10**9+1, 0)

    # 찾으려는 범위가 트리 범위에 속할 때
    if a <= start and end <= b:
        return segment[idx]

    mid = (start + end) // 2
    left = find(idx * 2, start, mid)
    right = find(idx * 2 + 1, mid + 1, end)
    return (min(left[0], right[0]), max(left[1], right[1]))


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

height = math.ceil(math.log2(N)) + 1
nodeCount = 1 << height

segment = [0 for _ in range(nodeCount)]
makeSegmentTree(1, 0, len(arr) - 1)

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1

    answer = find(1, 0, len(arr) - 1)
    print(answer[0], answer[1])
