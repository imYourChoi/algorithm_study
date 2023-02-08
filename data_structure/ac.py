# https://www.acmicpc.net/problem/5430

from collections import deque

answer = []

for _ in range(int(input())):
    ops = input()
    length = int(input())
    i = input().strip("[]").split(",")
    if i[0] == '':
        i = []
    else:
        i = list(map(int, i))
    nums = deque(i)
    reverse = False
    flag = True
    for op in ops:
        if op == "R":
            reverse = not reverse
        else:
            if not nums:
                answer.append("error")
                flag = False
                break
            if reverse:
                nums.pop()
            else:
                nums.popleft()
    if flag:
        if reverse:
            answer.append(str([*nums][::-1]).replace(" ",""))
        else:
            answer.append(str([*nums]).replace(" ",""))

print(*answer, sep="\n")