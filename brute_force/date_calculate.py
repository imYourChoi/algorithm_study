# https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())
answer = 1

while (True):
  if not ((answer - E) % 15 != 0 or (answer - S) % 28 != 0 or (answer - M) % 19 != 0): break
  answer += 1

print(answer)