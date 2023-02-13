# https://www.acmicpc.net/problem/10610

n = input()
if "0" not in n or sum(map(int, list(n))) % 3:
    print(-1)
else:
    print("".join(sorted(list(n), reverse=True)))