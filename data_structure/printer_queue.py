# https://www.acmicpc.net/problem/1966

from collections import deque

for _ in range(int(input())):
    n,m = map(int, input().split())
    array = [*map(int, input().split())]
    elem = array[m]
    array[m] = 0
    count = 1
    largest = max(array)
    queue = deque(array)
    while queue:
        f = queue.popleft()
        if not f:
            if largest > elem:
                queue.append(f)
            else:
                print(count)
                break
        elif f == largest:
            count += 1
            largest = max(max(queue), elem)
        else:
            queue.append(f)
