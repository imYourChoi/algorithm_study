# https://www.acmicpc.net/problem/1049

import math
n,m = map(int,input().split())
strings = [list(map(int,input().split())) for _ in range(m)]
inf = float('inf')
over,package,remain,each = inf,inf,inf,inf
for six,one in strings:
    over = min(over, math.ceil(n/6)*six)
    package = min(package,n//6*six)
    remain = min(remain,n%6*one)
    each = min(each,n*one)
print(min(over,package+remain, each))