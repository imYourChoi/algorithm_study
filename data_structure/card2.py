# https://www.acmicpc.net/problem/2164

from collections import deque
array = deque([x+1 for x in range(int(input()))])

while len(array) != 1:
    array.popleft()
    array.append(array.popleft())
print(array[0])