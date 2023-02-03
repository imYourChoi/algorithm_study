# https://www.acmicpc.net/problem/1918

equation = input()

stack = []

def priority(op):
    if op in ['(', ')']:
        return 0
    elif op in ['+', '-']:
        return 1
    else:
        return 2

for char in equation:
    if char.isalpha():
        print(char, end='')
    else:
        if char in ["+", "-", "*", "/"]:
            while stack and priority(char) <= priority(stack[-1]):
                print(stack.pop(), end='')
            stack.append(char)
        elif char == "(":
            stack.append("(")
        elif char == ")":
            op = stack.pop()
            while op != "(":
                print(op, end="")
                op = stack.pop()
while stack:
    print(stack.pop(), end="")
print()