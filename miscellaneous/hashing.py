# https://www.acmicpc.net/problem/15829

n = int(input())
s = input()
answer = 0
for idx, char in enumerate(s):
    answer += (ord(char) - 96) * 31 ** idx % 1234567891
print(answer % 1234567891)