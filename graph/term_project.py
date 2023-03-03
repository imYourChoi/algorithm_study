# https://www.acmicpc.net/problem/9466

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

answer = []

def dfs(index):
    global together
    visited[index] = True
    if not visited[choice[index]]:
        dfs(choice[index])
    else:
        if choice[index] not in team:
            next = choice[index]
            while next != index:
                together += 1
                next = choice[next]
            together += 1
    team.add(index)

for _ in range(int(input())):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    team = set()
    together = 0

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
    
    answer.append(n-together)

print(*answer, sep="\n")