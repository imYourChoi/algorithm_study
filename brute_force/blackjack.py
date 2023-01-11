# https://www.acmicpc.net/problem/2798

N, M = map(int, input().split())
array = sorted(list(map(int, input().split())))
answer = 0
for k in range(2, N):
    for j in range(1,k):
        for i in range(0,j):
            s = array[i] + array[j] + array[k] 
            if answer < s <= M:
                answer = s
print(answer)