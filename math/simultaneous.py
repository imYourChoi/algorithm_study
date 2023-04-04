# https://www.acmicpc.net/problem/19532

a,b,c,d,e,f = map(int, input().split())
def sim():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x+b*y == c and d*x + e*y == f:
                return x,y
print(*sim())