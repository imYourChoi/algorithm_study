# https://www.acmicpc.net/problem/1744

n = int(input())
arr = sorted([int(input()) for _ in range(n)])

minus = sorted([x for x in arr if x < 1], reverse=True)
plus = [x for x in arr if x > 0]

answer = 0

while plus:
    if len(plus) == 1:
        answer += plus.pop()
    else:
        first, second = plus.pop(), plus.pop()
        if 1 in [first,second]:
            answer += first + second
        else:
            answer += first * second

while minus:
    if len(minus) == 1:
        answer += minus.pop()
    else:
        first, second = minus.pop(), minus.pop()
        if 1 in [first,second]:
            answer += first + second
        else:
            answer += first * second

print(answer)