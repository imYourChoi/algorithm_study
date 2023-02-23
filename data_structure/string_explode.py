# https://www.acmicpc.net/problem/9935

string = input()
explode = input()
explodeLen = len(explode)
explodeSet = set(list(explode))

answer = ""

def check():
    while True:
        if "".join(stack[-explodeLen:]) == explode:
            for _ in range(explodeLen):
                stack.pop()
        else:
            break

for char in string:
    stack.append(char)
    if char == explode[-1]:
        check()

print("".join(stack) if stack else "FRULA")