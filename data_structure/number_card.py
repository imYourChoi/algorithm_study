# https://www.acmicpc.net/problem/10815

N = int(input())
cards = set(map(int, input().split()))
M = int(input())
print(*[1 if x in cards else 0 for x in map(int, input().split())], sep=" ")