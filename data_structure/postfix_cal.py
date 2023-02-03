# https://www.acmicpc.net/problem/1935

# https://www.acmicpc.net/problem/1918
# 위 문제의 연장선 -> 후위 표기식 계산법

n = int(input())
equation = input()
nums = {}
for i in range(n):
    nums[i+65] = int(input())
stack=[]
for char in equation:
    if char.isalpha():
        stack.append(char)
    else:
        second = stack.pop()
        first = stack.pop()
        if str(first).isalpha():
            first = nums[ord(first)]
        if str(second).isalpha():
            second = nums[ord(second)]
        temp = 0
        if char == "+":
            temp = first + second
        if char == "-":
            temp = first - second
        if char == "*":
            temp = first * second
        if char == "/":
            temp = first / second
        stack.append(temp)

print("%.2f" % stack[0])