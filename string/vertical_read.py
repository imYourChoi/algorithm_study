# https://www.acmicpc.net/problem/10798

a = [input() for _ in range(5)]
l = len(max(a,key=len))
a = [each.ljust(l) for each in a]
word = ""
for words in zip(*a):
    word += "".join(words)

print(word.replace(" ", ""))
