# https://www.acmicpc.net/problem/1080

N,M = map(int,input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

def switch(y,x):
    for Y in range(y,y+3):
        for X in range(x,x+3):
            A[Y][X] = 1 - A[Y][X]

def traverse():
    answer = 0
    for y in range(N-2):
        for x in range(M-2):
            if A[y][x] != B[y][x]:
                switch(y,x)
                answer += 1
        if A[y][-1] != B[y][-1] or A[y][-2] != B[y][-2]:
            return -1
    for y in range(N-2, N):
        for x in range(M):
            if A[y][x] != B[y][x]:
                return -1
    return answer

if N < 3 or M < 3:
    flag = False
    for a,b in zip(A,B):
        for aa, bb in zip(a,b):
            if aa != bb:
                flag = True
    if flag:
        print(-1)
    else: print(0)
else:
    print(traverse())