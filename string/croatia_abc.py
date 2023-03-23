# https://www.acmicpc.net/problem/2941

alph = ["c=","c-","dz=","d-","lj","nj","s=","z="]

s = input()
for each in alph:
    while each in s:
        s = s.replace(each, "a")

print(len(s))