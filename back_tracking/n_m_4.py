# https://www.acmicpc.net/problem/15652

n,m = map(int, input().split())

def nm(array, seq, index):
    if index == 1:
        for num in array:
            if not seq or (seq and not seq[-1] > num):
                print(*seq, num)
    else:
        for num in array:
            if not seq or (seq and not seq[-1] > num):
                nm(array, seq + [num], index-1)

nm([x+1 for x in range(n)], [], m)