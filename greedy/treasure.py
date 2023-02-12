# https://www.acmicpc.net/problem/1026

n = int(input())
A,B = map(int, input().split()), map(int, input().split())

print(sum([a*b for a,b in zip(sorted(A), sorted(B, reverse=True))]))