# https://www.acmicpc.net/problem/1107

n = int(input())
broNum = int(input())
if broNum == 0:
    print(min(len(str(n)), abs(n - 100)))
    exit(0)
broken = set(input().split())

def upperAndLower(num):
    upTemp = num
    lowTemp = num
    upValid, lowValid = False, False
    while True:
        if set([*str(upTemp)]) & broken:
            upTemp += 1
        else:
            upValid = True
            
        if lowTemp >= 0:
            if set([*str(lowTemp)]) & broken:
                lowTemp -= 1
            else:
                lowValid = True
        if upValid or lowValid:
            break
    if lowTemp < 0:
        return abs(upTemp - num) + len(str(upTemp))
    return min(abs(upTemp - num) + len(str(upTemp)), abs(num - lowTemp) + len(str(lowTemp)))

if broNum == 10:
    print(abs(n-100))
else:
    print(min(upperAndLower(n), abs(n - 100)))