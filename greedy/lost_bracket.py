# https://www.acmicpc.net/problem/1541

nums = [*input()]
answer = 0
temp = ""
minus = False
for char in nums:
    if char == "+":
        if not minus:
            answer += int(temp)
            temp = ""
        else:
            answer -= int(temp)
            temp = ""
    elif char == "-":
        if not minus:
            answer += int(temp)
            temp = ""
        else:
            answer -= int(temp)
            temp = ""
        minus = True
    else:
        temp += char

if not minus:
    answer += int(temp)
    temp = ""
else:
    answer -= int(temp)
    temp = ""

print(answer)