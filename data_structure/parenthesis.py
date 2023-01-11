# https://www.acmicpc.net/problem/9012

n = int(input())

for _ in range(n):
    s = input()
    a = []
    flag = True
    for c in s:
        if c == "(":
            a.append(c)
        else:
            if a:
                a.pop()
            else:
                print("NO")
                flag = False
                break
    if a:
        print("NO")
        continue
    if flag:
        print("YES")