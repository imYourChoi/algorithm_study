# https://www.acmicpc.net/problem/12851

from collections import deque

N, M = map(int, input().split())
visited = [False] * 100001

def check(origin, position, newDict, curDict, dest):
    if 0 <= position <= 100000 and not visited[position]:
        if position in newDict:
            newDict[position] += curDict[origin]
        else:
            newDict[position] = curDict[origin]
    if position == dest:
        return True
    else: return False

def bfs(N, M):
    if N == M:
        return 0, 1
    second = 0
    curDict = {N:1}
    visited[N] = True

    while curDict:
        newDict = {}
        second += 1
        temp = False
        for current in curDict:
            temp |= check(current, current - 1, newDict, curDict, M)
            temp |= check(current, current + 1, newDict, curDict, M)
            temp |= check(current, current * 2, newDict, curDict, M)
        for key in newDict:
            visited[key] = True
        if temp:
            return second, newDict[M]
        curDict = newDict

print(*bfs(N, M), sep="\n")