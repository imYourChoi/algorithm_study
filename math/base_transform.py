# https://www.acmicpc.net/problem/2745

B, N = input().split()
N = int(N)
answer = 0
for pos, char in enumerate(B[::-1]):
    pos = int(pos)
    if char.isnumeric(): answer += N ** pos * int(char)
    else: answer += N ** pos * (ord(char) - 55)
print(answer)