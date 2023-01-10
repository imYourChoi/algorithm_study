import sys
sys.setrecursionlimit(10 ** 6)
array = [int(input()) for _ in range(int(input()))]

def quick(array, low, high):
    if low >= high: return
    tempL = low + 1
    tempH = high
    pivot = low
    while tempL <= tempH:
        while tempL <= high and array[tempL] < array[pivot]:
            tempL += 1
        while tempH > low and array[tempH] > array[pivot]:
            tempH -= 1
        if tempL > tempH:
            array[tempH], array[low] = array[low], array[tempH]
        else:
            array[tempL], array[tempH] = array[tempH], array[tempL]

    quick(array, low, tempH-1)
    quick(array, tempH+1, high)

quick(array, 0, len(array) - 1)

for x in array:
    print(x)