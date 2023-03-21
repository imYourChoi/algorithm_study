# https://www.acmicpc.net/problem/1316

answer = 0

def check():
    word = input()
    temp = word[0]
    d = set(temp)
    for c in word[1:]:
        if c == temp:
            continue
        if c in d:
            return 0
        else:
            d.add(c)
            temp = c
    return 1

for _ in range(int(input())):
    answer += check()

print(answer)