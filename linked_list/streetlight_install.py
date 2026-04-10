# https://www.codetree.ai/ko/frequent-problems/samsung-sw/problems/street-light-installation/description

import heapq

Q = int(input())

_, N, M, *lights = map(int, input().split())

street = {}

for i, light in enumerate(lights):
    street[light] = [None, None]

    if i > 0:
        street[light][0] = lights[i-1]
    if i < M - 1:
        street[light][1] = lights[i+1]

street[lights[0]][0] = 0
street[lights[-1]][1] = N + 1

heap = []

for light in lights:
    prev, next = street[light]
    if next != N + 1:
        heapq.heappush(heap, (-(next-light-1), light, next))


lightSet = set(lights)

left, right = lights[0], lights[-1]

for _ in range(Q-1):
    command, *rest = map(int, input().split())
    # print(street)
    # print(heap)
    if command == 400:
        # print("400")

        while heap[0][1] not in lightSet or heap[0][2] not in lightSet or street[heap[0][1]][1] != heap[0][2] or street[heap[0][2]][0] != heap[0][1]:
            dist, prev, next = heapq.heappop(heap)

        print(int(max(left-1, N-right, (-heap[0][0] + 1) / 2) * 2))

        # print()

    if command == 200:
        # print("200")

        dist, prev, next = heap[0]

        while heap[0][1] not in lightSet or heap[0][2] not in lightSet or street[heap[0][1]][1] != heap[0][2] or street[heap[0][2]][0] != heap[0][1]:
            dist, prev, next = heapq.heappop(heap)

        dist, prev, next = heapq.heappop(heap)

        mid = (prev + next + 1) // 2

        street[prev][1] = mid
        street[next][0] = mid

        street[mid] = [prev, next]

        heapq.heappush(heap, (-(mid-prev-1), prev, mid))
        heapq.heappush(heap, (-(next-mid-1), mid, next))

        lights.append(mid)
        lightSet.add(mid)

        # print(street)
        # print()

    if command == 300:
        # print("300")

        num = lights[rest[0]-1]
        lightSet.remove(num)

        prev, next = street[num]

        if prev == 0:
            street[next][0] = 0
            left = next
        elif next == N+1:
            street[prev][1] = N+1
            right = prev
        else:
            street[next][0] = prev
            street[prev][1] = next
            heapq.heappush(heap, (-(next-prev-1), prev, next))

        street.pop(num)
        # print()
