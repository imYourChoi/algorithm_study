# https://www.acmicpc.net/problem/11000

import sys, heapq
input = sys.stdin.readline

n = int(input())
rooms = [tuple(map(int, input().split())) for _ in range(n)]
rooms.sort(key=lambda x:x[0])

answer = 1
current_rooms = [rooms[0][1]]
for room in rooms[1:]:
    if current_rooms[0] > room[0]:
        heapq.heappush(current_rooms, room[1])
        answer = max(answer, len(current_rooms))
    else:
        heapq.heappop(current_rooms)
        heapq.heappush(current_rooms, room[1])
    print(current_rooms)
print(answer)