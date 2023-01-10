# https://www.acmicpc.net/problem/16928

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
array = [[False, 0] for _ in range(101)]

for _ in range(N+M):
    start, end = map(int, input().split())
    array[start][1] = end

def bfs():
    count = 0
    array[1][0] = True
    queue = deque([1])

    while queue:
        # print(queue)
        count += 1
        for _ in range(len(queue)):
            current = queue.popleft()
            dice = 0
            for i in range(current + 1, current + 7):
                if i == 100:
                    return count

                if array[i][0]:
                    continue
                array[i][0] = True

                if array[i][1]:
                    if array[array[i][1]][0]:
                        continue
                    queue.append(array[i][1])
                    continue
                if not array[i][1]:
                    array[i][0] = True
                    dice = i
            if dice:
                array[dice][0] = True
                queue.append(dice)

print(bfs())