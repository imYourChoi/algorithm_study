# https://www.acmicpc.net/problem/24060

size, save = map(int, input().split())
array = [int(x) for x in input().strip().split()]
order = 0
num = 0

def merge_sort(array, l, r):
    if (l >= r): return
    m = (l + r) // 2
    merge_sort(array, l, m)
    merge_sort(array, m+1, r)
    merge(array, l, r)

def merge(array, l, r):
    temp = array[l:r+1]
    m = (l + r) // 2
    left = 0
    right = m - l + 1
    for i in range(l,r + 1):
        if left > m - l:
            array[i] = temp[right]
            right += 1
        elif right > r - l:
            array[i] = temp[left]
            left += 1
        elif temp[left] < temp[right]:
            array[i] = temp[left]
            left += 1
        else:
            array[i] = temp[right]
            right += 1
        global order
        global num
        order += 1
        if order == save:
            num = array[i]

merge_sort(array, 0, size - 1)

if num > 0:
    print(num)
else:
    print(-1)