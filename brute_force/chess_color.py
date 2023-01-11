# https://www.acmicpc.net/problem/1018

N, M = map(int, input().split())
array = [[*input()] for _ in range(N)]

def chess(row,column):
    temp = 0
    for r in range(row, row+8):
        for c in range(column, column+8):
            if (r+c)%2==0 and array[r][c] == "B": temp += 1
            if (r+c)%2==1 and array[r][c] == "W": temp += 1
    return 64 - max(temp, 64-temp)

answer = 32
for r in range(N-8+1):
    for c in range(M-8+1):
        answer = min(answer, chess(r,c))
print(answer)