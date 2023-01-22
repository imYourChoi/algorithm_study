# https://www.acmicpc.net/problem/10799

string = input().split("()")
stack = []
answer = 0

for rod in string:
    for each in rod:
        if each == "(":
            stack.append(1)
        if each == ")":
            stack.pop()
            answer += 1
    answer += len(stack)

print(answer)