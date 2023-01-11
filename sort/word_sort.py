# https://www.acmicpc.net/problem/1181

N = int(input())

# d = {}
# for i in range(N):
#     word = input()
#     if len(word) in d:
#         d[len(word)].add(word)
#     else:
#         d[len(word)] = {word}

# for key in sorted(d):
#     print("\n".join(sorted(d[key])))

array=list(set([input() for _ in range(N)]))
array.sort()
array.sort(key=len)

print("\n".join(array))