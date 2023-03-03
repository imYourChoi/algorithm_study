# https://www.acmicpc.net/problem/1978

answer = int(input())
for num in list(map(int, input().split())):
    if num == 1:
        answer -= 1
        continue
    for i in range(2,int((num ** 0.5)) // 1 + 1):
        if num % i == 0:
            answer -= 1
            break
print(answer)
            
