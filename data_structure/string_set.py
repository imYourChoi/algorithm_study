# https://www.acmicpc.net/problem/14425

N,M = map(int, input().split())
S = set([input() for _ in range(N)])
print(sum([1 if input() in S else 0 for _ in range(M)]))