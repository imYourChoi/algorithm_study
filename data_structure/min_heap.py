# https://www.acmicpc.net/problem/1927

import sys
input=sys.stdin.readline

n = int(input())

array = []

def heapify(index):
    if not array:
        pass
    else:
        smallest = index
        left = index * 2 + 1
        right = index * 2 + 2
        if left < len(array) and array[left] < array[smallest]:
            smallest = left
        if right < len(array) and array[right] < array[smallest]:
            smallest = right
        if smallest != index:
            array[index], array[smallest] = array[smallest], array[index]
            heapify(smallest)

def heapify_up(index):
    if index == 0:
        return
    up = (index + 1) // 2 - 1
    if array[up] > array[index]:
        array[index], array[up] = array[up], array[index]
        heapify_up(up)

def pop():
    if not array:
        print(0)
    else:
        array[0], array[-1] = array[-1], array[0]
        print(array.pop())
        heapify(0)
    

for _ in range(n):
    # print(array)
    num = input().rstrip()
    if num == '0':
        pop()
    else:
        array.append(int(num))
        heapify_up(len(array)-1)