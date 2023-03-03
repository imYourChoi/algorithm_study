# https://www.acmicpc.net/problem/1065

n = int(input())
answer = 0

def arith(arr):
    diff = arr[1] - arr[0]
    for j in range(1,len(arr)-1):
        if arr[j+1] - arr[j] != diff:
            return 0
    return 1


for i in range(1,n+1):
    arr = list(map(int, [*str(i)]))
    if len(arr) <= 1:
        answer += 1
        continue
    answer += arith(arr)
    
print(answer)