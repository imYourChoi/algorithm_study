# https://www.acmicpc.net/problem/1339

n = int(input())
array = [input() for _ in range(n)]
length = len(max(array, key=len))
array = [x.rjust(length, "=") for x in array]
d = {}
for idx, zipped in enumerate(zip(*array)):
    for char in zipped:
        if char == "=":
            continue
        d[char] = d.get(char,0) + (10**(length-idx-1))
answer = 0
for idx, x in enumerate(sorted(d.items(), key=lambda x:x[1], reverse=True)):
    answer += x[1] * (9-idx)
print(answer)