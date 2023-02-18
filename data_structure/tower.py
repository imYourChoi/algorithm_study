# https://www.acmicpc.net/problem/2493

n = int(input())
towers = list(map(int,input().split()))

answer = [0] * n
stack = []

for idx in range(n,0,-1):
    if not stack:
        stack.append((towers[idx-1], idx))
    else:
        while stack and towers[idx-1] > stack[-1][0]:
            height, position = stack.pop()
            answer[position-1] = idx
        stack.append((towers[idx-1], idx))

print(*answer)
