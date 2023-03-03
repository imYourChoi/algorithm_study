# https://www.acmicpc.net/problem/1157

word = input()
d = {}
for char in word.lower():
    d[char] = d.get(char,0)+1
s = sorted(list(d.items()),key=lambda x:x[1])
print("?" if len(s) > 1 and s[-2][1] == s[-1][1] else s[-1][0].upper())