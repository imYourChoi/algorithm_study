# https://www.acmicpc.net/problem/1920

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())

def binary_search(num, start, end):
    mid = (start + end) // 2
    if A[mid] == num:
        return 1
    elif start >= end:
        return 0
    elif A[mid] > num:
        return binary_search(num, start, mid-1)
    else:
        return binary_search(num, mid+1, end)

for num in list(map(int, input().split())):
    print(binary_search(num, 0, N - 1))