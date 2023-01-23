# https://www.acmicpc.net/problem/15651

a, b = map(int, input().split())

def series(array, string, index):
    if index == 1:
        for num in array:
            p = "%s %d" % (string, num)
            print(p.strip())
    else:
        for num in array:
            series(array, "%s %d" % (string, num), index-1)

series([x+1 for x in range(a)], "", b)