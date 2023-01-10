import sys
sys.setrecursionlimit(10 ** 6)
array = [int(input()) for _ in range(int(input()))]

def heapify(array, i, n):
    if i * 2 + 1 > n - 1:
        return
    temp = i
    if array[i] < array[i * 2 + 1]:
        temp = i * 2 + 1
    if i * 2 + 2 < n and array[temp] < array[i * 2 + 2]:
        temp = i * 2 + 2
    if temp != i:
        array[i], array[temp] = array[temp], array[i]
        heapify(array, temp, n)
    # print(array)
    

for i in range(len(array) // 2 - 1, -1, -1):
    heapify(array, i, len(array))

for i in range(len(array)-1, 0, -1):
    array[i], array[0] = array[0], array[i]
    heapify(array, 0, i)

for x in array:
    print(x)