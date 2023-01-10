# https://www.acmicpc.net/problem/15649
# 순열 구하는 문제

a, b = map(int, input().split())

def series(array, string, index):
    if index == 1:
        for num in array:
            p = "%s %d" % (string, num)
            print(p.strip())
    else:
        for num in array:
            if num in map(int, string.split()): return
            newArray = array.copy()
            newArray.remove(num)
            series(newArray, "%s %d" % (string, num), index-1)

series([x+1 for x in range(a)], "", b)