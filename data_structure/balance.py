# https://www.acmicpc.net/problem/4949

while True:
    s = input()
    if s == ".":
        break
    stack = []
    flag = False
    for char in s:
        if flag:
            break
        if char == ".":
            if stack:
                print("no")
            else:
                print("yes")
            flag = True
        elif char in ["[", "("]:
            stack.append(char)
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                flag = True
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                flag = True