# https://www.acmicpc.net/problem/10812

N,M = map(int, input().split())
array = [x+1 for x in range(N)]
for _ in range(M):
    i,j,k = map(int, input().split())
    temp = array[k-1:j] + array[i-1:k-1]
    for idx in range(i-1,j):
        array[idx] = temp[idx-i+1]
print(*array)